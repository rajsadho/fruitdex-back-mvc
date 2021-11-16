import os
from flask import Flask
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta 


from flask_uploads import (
    UploadSet, 
    configure_uploads, 
    IMAGES, 
    TEXT, 
    DOCUMENTS
)


# Initialize Database and register Models

db = SQLAlchemy()
from App.models import *



# Register Views

from App.views import (
    api_views,
    user_views
)

views = [api_views, user_views]

def add_views(app, views):
    for view in views:
        app.register_blueprint(view)


# Setup JWT

''' Set up JWT here (if using flask JWT)'''
def authenticate(email, password):
  user = User.query.filter_by(email=email).first()
  if user and user.check_password(password):
    return user

#Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
  return User.query.get(payload['identity'])


''' End JWT Setup '''

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
        app.config['JWT_EXPIRATION_DELTA'] = os.environ.get('JWT_EXPIRATION_DELTA')
        app.config['DEBUG'] = os.environ.get('DEBUG')
        app.config['ENV'] = os.environ.get('ENV')


def create_app(config={}):
    app = Flask(__name__, static_url_path='/static')
    loadConfig(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    app.config.update(config)
    db.init_app(app)
    add_views(app, views)  
    jwt = JWT(app, authenticate, identity)
    app.app_context().push()
    return app

from App.controllers import *
from App.tests import *