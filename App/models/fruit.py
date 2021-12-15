from App.models import db


class Fruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wiki_uri = db.Column(db.String)
    tags = db.relationship("Tag", backref="fruits")
    names =  db.relationship("FruitName", backref="fruits")
    images = db.relationship("Image", backref="fruits")

    def toDict(self):
        return{
            'id': self.id,
            'wiki_uri': self.wiki_uri,
            'names': [n.toDict() for n in self.names],
            'tags': [t.toDict() for t in self.tags],
            'images': [i.toDict() for i in self.images]
        }
    
    def __repr__(self):
        return '<Fruit {}>'.format(self.wiki_uri) 