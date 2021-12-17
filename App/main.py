import os
from flask import Flask
from flask_jwt import JWT
from datetime import timedelta
from flask_cors import CORS

from App.models import db, User

from flask_uploads import (
    UploadSet, 
    configure_uploads, 
    IMAGES, 
    TEXT, 
    DOCUMENTS
)

from App.views import (
    api_views,
    user_views,
    fruit_views,
    image_views
)

#place all views here
views = [api_views, user_views, fruit_views, image_views]

def add_views(app, views):
    for view in views:
        CORS(view, resources={r'/*': {'origins': '*'}})
        app.register_blueprint(view)

def loadConfig(app):
    
    app.config['ENV'] = os.environ.get('ENV', 'development')
    if app.config['ENV'] == "development":
        app.config.from_object('App.config')
    else:
        uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = uri
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        val = os.environ.get('JWT_EXPIRATION_DELTA')
        if isinstance(val, (str)):
            val = int(val)
        app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=val)
        app.config['DEBUG'] = os.environ.get('DEBUG')
        app.config['ENV'] = os.environ.get('ENV')

''' Set up JWT here (if using flask JWT)'''
def authenticate(username, password):
  user = User.query.filter_by(username=username).first()
  if user and user.check_password(password):
    return user

#Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
  return User.query.get(payload['identity'])


''' End JWT Setup '''

def init_db(app):
    db.init_app(app)
    db.create_all(app=app)

def create_app(config={}):
    app = Flask(__name__, static_url_path='/static')
    loadConfig(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    app.config['CORS_HEADERS'] = 'Content-Type'
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    app.config.update(config)
    db.init_app(app)
    add_views(app, views)  
    jwt = JWT(app, authenticate, identity)
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.app_context().push()

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Access-Control-Allow-Credentials')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    return app

if __name__ == "__main__":
    app = create_app()