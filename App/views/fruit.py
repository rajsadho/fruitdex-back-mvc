from flask import Blueprint, request, jsonify
from flask_login import LoginManager, current_user, login_user, login_required,logout_user
from sqlalchemy.sql.operators import json_getitem_op

fruit_views = Blueprint('fruit_views', __name__, template_folder='../templates')

from App.controllers import (get_all_fruits_json, 
    get_fruit_dict_by_name,
    create_image,get_fruit_by_tag)


@fruit_views.route('/api/fruits',methods=["GET"])
def get_all_fruits():
    fruits=get_all_fruits_json()
    return jsonify(fruits=fruits)

@fruit_views.route('/api/fruits/search',methods=["GET"])
def search():
    args = request.args
    if "name" in args:
        fruit=get_fruit_dict_by_name(args["name"])
        return jsonify(fruit)
    else:
        return jsonify(message="No query entered"), 400

@fruit_views.route('/upload',methods=["POST"])
@login_required
def upload():
    data=request.json
    create_image(data['uri'],data['text'],0,0)
    return ('UPLOADED')

@fruit_views.route('/filter',methods=["GET"])
def filter(tag):
    fruits=get_fruit_by_tag(tag)
    fruits=[fruit.toDict() for fruit in fruits]
    return fruits


    