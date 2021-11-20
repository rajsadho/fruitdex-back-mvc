from flask import redirect, render_template, request, url_for, jsonify

from App.models import ( fruit_name, db )

def get_all_fruitNames_json():
    fruits=fruit_name.query.all()
    if not fruits:
        return[]
    fruits=[fruits.toDict()for fruit in fruits]
    return fruits

def create_fruit(name,name_type):
    fruit=fruit_name(name=name,name_type=name_type)
    db.session.add(fruit)
    db.session.commit()

def create_fruits(fruits):
    for fruit in fruits:
        newfruit=fruit_name(name=fruit['name'],name_type=fruit['name_type'])
        db.session.add(newfruit)
    db.session.commit()

def get_fruit_by_name(name):
    return fruit_name.query.filter_by(name=name).first()

def get_fruit_by_nametype(name_type):
    return fruit_name.query.filter_by(name_type=name_type).first()