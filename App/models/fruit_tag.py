from sqlalchemy.sql.schema import Column
from App.models import db

class FruitTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fruit_id = db.Colum(db.Integer, db.ForeignKey('fruit.id'), primary_key=True)
    tag_id = db.Colum(db.Integer, db.ForeignKey('tag.id'), primary_key=True)

    extra_data = db.Colum(db.String(50))

    fruit = db.relationship('Fruit', backref='tags')
    tag =db. relationship('Tag', backref='fruits')