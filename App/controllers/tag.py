from flask import redirect, render_template, request, url_for, jsonify

from App.models import ( Tag, db )

def get_all_tags_json():
    tags = Tag.query.all()
    if not tags:
        return[]
    tags = [tag.toDict() for tag in tags]
    return tags

def create_tag(value, tag_type, description):
    tag = tag(value=value, tag_type=tag_type, description=description)
    db.session.add(tag)
    db.session.commit()

def create_tags(tags):
    for tag in tags:
        newTag = tag(value=tag['value'], tag_type=tag['tag_type'], description=tag['description'])
        db.session.add(newTag)
    db.session.commit()

def get_tag_by_id(id):
    return Tag.query.get(id)

def get_tag_by_value(value):
    return Tag.query.filter_by(value=value).first()