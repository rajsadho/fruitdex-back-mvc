from sqlalchemy.orm import backref
from sqlalchemy.schema import UniqueConstraint
from App.models import db


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target_table = db.Column(db.String)
    target_id = db.Column(db.String)
    
    reporter_id = db.Column(db.ForeignKey('user.id'))
    reporter = db.relationship("User", backref="report")

    UniqueConstraint(reporter_id, target_id, target_table, name="uxc_0")


    def toDict(self):
        return{
            'id': self.id,
            'target_table': self.target_table,
            'target_id': self.target_id,
            'reporter_id': self.reporter_id
        }
    
    def __repr__(self):
        return '<Report {}>'.format(self.id) 
