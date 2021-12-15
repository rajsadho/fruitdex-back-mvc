from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.controllers import (get_all_fruits,get_fruit_by_name,create_image,get_fruit_by_tags)


@user_views.route('/fruits',methods=['GET'])
def get_all_fruits():
    fruits=get_all_fruits()
    return render_template('index.html',fruits=fruits)

@user_views.route('/search/<fruitName>',methods=['GET'])
def search(fruitName):
    fruit=get_fruit_by_name(fruitName)
    return render_template('index',fruit=fruit)

@user_views.route('/upload',methods=['POST'])
def upload():
    data=request.json
    create_image(data['uri'],data['text'],0,0)
    return ('UPLOADED')

@use_views.route('/filter',methods='GET')
def filter(tag):
    fruits=get_fruit_by_tags(tag)
    return render_template('index',fruits=fruits)


    