from flask import redirect, render_template, request, url_for, jsonify

from App.models import ( Fruit, db )


def create_fruit(wiki_uri,names,images):
    fruit=fruit(wiki_uri=wiki_uri,names=names,images=images)
    db.session.add(fruit)
    db.commit()

def create_fruits(fruits):
    for fruit in fruits:
        newfruit=fruit(wiki_uri=fruit['wiki_uri'],names=fruit['names'],images=fruit['images'])
        db.session.add(newfruit)
    db.session.commit()

def get_all_fruits_json():
    fruits=Fruit.query.all()
    if not fruits:
        return []
    fruits=[fruits.toDict() for fruit in fruits]
    return fruits

def get_all_fruits():
    return Fruit.query.all()

def get_fruit_by_name(name):
    return fruit.query.filter_by(names=name).first()

def get_fruit_by_tags(tag):
    return Fruit.query.filter_by(tag=tag).all()



