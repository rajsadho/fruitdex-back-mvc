from datetime import timedelta

SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
SECRET_KEY = "secret key"
JWT_EXPIRATION_DELTA = timedelta(days=7)
DEBUG = True
ENV = "development"
