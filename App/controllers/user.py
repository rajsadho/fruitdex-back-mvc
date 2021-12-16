from flask import redirect, render_template, request, url_for, jsonify

from App.models import ( User, db )

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

def create_users(users):
    for user in users:
        newuser = User(username=user['username'], email=user['email'])
        newuser.set_password(user['password'])
        db.session.add(newuser)
    db.session.commit()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_all_users():
    return  User.query.all()