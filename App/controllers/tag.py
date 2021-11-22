from flask import redirect, render_template, request, url_for, jsonify

from App.models import ( Tag, db )

def get_all_tags_json():
    tags = Tag.query.all()
    if not tags:
        return[]
    tags = [tag.toDict() for tag in tags]
    return tags

