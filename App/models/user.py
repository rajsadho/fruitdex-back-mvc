import datetime
from enum import unique

from App.models import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    reports = db.relationship("Report", backref="user")
    images = db.relationship("Image", backref="user")

    def toDict(self):
        return{
            'id': self.id,
            'username': self.first_name,
            'email': self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.email) 