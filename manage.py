from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from App.main import create_app
from App.models import db, User
from App.controllers import create_users

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

# add migrate command
manager.add_command('db', MigrateCommand)

# initDB command
@manager.command
def initDB():
    db.create_all(app=app)
    print('database initialized!')

# serve command
@manager.command
def serve():
    print('Application running in '+app.config['ENV']+' mode')
    app.run(host='0.0.0.0', port=8080, debug=app.config['ENV']=='development')

@manager.command
def make_users():
    create_users()
    print("users created")

if __name__ == "__main__":
    manager.run()
