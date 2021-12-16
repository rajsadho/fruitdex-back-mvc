from sqlalchemy.orm import backref
from App.models import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.String(200))
    alt_text = db.Column(db.String(255))
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)

    uploader_id = db.Column(db.ForeignKey('user.id'))
    uploader = db.relationship("User", backref="image")
    
    fruit_id = db.Column(db.ForeignKey('fruit.id'))
    fruit = db.relationship("Fruit", backref="image")


    def toDict(self):
        return{
            'id': self.id,
            'uri': self.uri,
            'alt_tex': self.alt_text,
            'upvotes': self.upvotes,
            'downvotes': self.downvotes,
            'uploader_id': self.uploader_id,
            'fruit_id': self.fruit_id
        }
    
    def __repr__(self):
        return '<Image {}>'.format(self.id) 
