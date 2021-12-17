from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required

from App.controllers.image import create_image

image_views = Blueprint('image_views', __name__, template_folder='../templates')

from App.controllers import (
    get_all_images_json,
    get_image_by_id_json
)

@image_views.route('/api/images',methods=["GET"])
def get_all_images():
    images=get_all_images_json()
    return jsonify(images=images)

@image_views.route('/api/images',methods=["POST"])
@jwt_required()
def add_image():
    args = request.json
    create_image(args)
    return jsonify(message='Created')

@image_views.route('/api/images/<image_id>',methods=["GET"])
def get_image_by_id(image_id):
    image=get_image_by_id_json(image_id)
    return jsonify(image=image)