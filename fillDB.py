from App.controllers import (create_tags, create_users, create_fruits, create_images)
import json

def read_json_file(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

def create_default_tags(filename):
    tags = read_json_file(filename)
    create_tags(tags['tags'])

def create_default_users(filename):
    users = read_json_file(filename)
    create_users(users['users'])

def create_default_fruits(filename):
    fruits = read_json_file(filename)
    create_fruits(fruits['fruits'])

def create_default_images(filename):
    images = read_json_file(filename)
    create_images(images['images'])
