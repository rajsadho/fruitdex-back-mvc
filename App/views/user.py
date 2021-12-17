from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory
from flask_login import LoginManager, current_user, login_user, login_required,logout_user

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.controllers import (
    get_all_users_json, 
    create_user, 
    get_user_json_by_id,
    get_images_by_user_id_json,
    get_user_by_username,
    get_user_by_email
    )

@user_views.route('/api/users')
def get_all_users():
    users = get_all_users_json()
    return jsonify(users=users)

@user_views.route('/api/users/<user_id>')
def get_user_by_id(user_id):
    user = get_user_json_by_id(user_id)
    return jsonify(user=user)

@user_views.route('/api/users/<user_id>/images')
def get_user_images(user_id):
    images = get_images_by_user_id_json(user_id)
    return jsonify(user_id=user_id, images=images)

@user_views.route('/signup',methods=["POST"])
def signup():
    data=request.json
    if get_user_by_username(data['username']):
        return jsonify(message='Username already in use'), 403
    if get_user_by_email(data['email']):
        return jsonify(message='Email already in use'), 403
    create_user(data['username'], data['email'], data['password'])
    return jsonify(message='Created')
