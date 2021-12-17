from App.models import db


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    tag_type = db.Column(db.String)

    fruits = db.relationship("FruitTag", back_populates="tag")
    
    def toDict(self):
        return{
            'id': self.id,
            'value': self.value,
            'tag_type': self.tag_type,
        }
    
    def __repr__(self):
        return '<Fruit {}>'.format(self.value) 