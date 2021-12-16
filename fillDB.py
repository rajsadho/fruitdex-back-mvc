from App.controllers.fruit import create_fruits
from App.models import (db, User, Fruit, Tag)
from App.controllers import (create_tags, create_users, create_fruits)
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
