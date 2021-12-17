from flask import Blueprint, request, jsonify
from flask_login import LoginManager, current_user, login_user, login_required,logout_user

image_views = Blueprint('image_views', __name__, template_folder='../templates')

from App.controllers import (
    get_all_images_json,
    get_image_by_id_json
)

@image_views.route('/api/images',methods=["GET"])
def get_all_images():
    images=get_all_images_json()
    return jsonify(images=images)

@image_views.route('/api/images/<image_id>',methods=["GET"])
def get_image_by_id(image_id):
    image=get_image_by_id_json(image_id)
    return jsonify(image=image)