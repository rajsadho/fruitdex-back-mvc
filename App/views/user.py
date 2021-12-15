from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory
from flask_login import LoginManager, current_user, login_user, login_required,logout_user

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.controllers import ( get_all_users_json, get_all_users,create_user )

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users')
def client_app():
    users = get_all_users()
    return jsonify(users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')


@user_views.route('/signup',methods=['POST'])
def signup():
    data=request.json
    create_user(data['fname'], data['lname'], data['email'], data['password'])
    return 'CREATED'

@user.views.route('/login',methods=['GET'])
def login():
    form = LogIn()
    if form.validate_on_submit(): 
      data = request.form
      user = User.query.filter_by(username = data['username']).first()
      if user and user.check_password(data['password']): 
        flash('Logged in successfully.') 
        login_user(user) 
        return redirect(url_for('index')) 
    flash('Invalid credentials')
    return redirect(url_for('login'))