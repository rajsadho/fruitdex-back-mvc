from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory
from flask_login import LoginManager, current_user, login_user, login_required,logout_user

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.controllers import ( get_all_users_json, create_user )

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/signup',methods=["POST"])
def signup():
    data=request.json
    create_user(data['username'], data['email'], data['password'])
    return 'CREATED'

@user_views.route('/login',methods=["GET"])
def login():
    return ""