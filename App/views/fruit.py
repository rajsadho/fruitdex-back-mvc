from flask import Blueprint, redirect, render_template, request, jsonify, send_from_directory

user_views = Blueprint('user_views', __name__, template_folder='../templates')

from App.controllers import (get_all_fruits,get_fruit_by_name)


@user_views.route('/fruits',methods=['GET'])
def get_all_fruits():
    fruits=get_all_fruits()
    return render_template('fruits.html',fruits=fruits)
    