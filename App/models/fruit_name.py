from App.models import db


class FruitName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    name_type = db.Column(db.String)

    fruit_id = db.Column(db.ForeignKey('fruit.id'))
    fruit = db.relationship("Fruit", backref="name")
    
    def toDict(self):
        return{
            'id': self.id,
            'fruit_id': self.fruit_id,
            'name': self.name,
            'name_type': self.name_type if self.name_type else "Secondary",
        }
    
    def __repr__(self):
        return '<Fruit {}>'.format(self.name) 