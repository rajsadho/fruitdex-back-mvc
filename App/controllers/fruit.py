from flask import redirect, render_template, request, url_for, jsonify

from App.models import ( Fruit, db )

def get_all_fruits_json():
    fruits=Fruit.query.all()
    if not fruits:
        return []
    fruits=[fruits.toDict() for fruit in fruits]
    return fruits

def get_all_fruits():
    return Fruit.query.all()

