from flask import redirect, render_template, request, url_for, jsonify

from App.models import ( Image, db )

def get_all_images_json():
    images=Image.query.all()
    if not image:
        return[]
    images=[images.toDict() for image in images]
    return images

def create_image(uri,alt_text,upvotes,downvotes):
    image=Image(uri=uri,alt_text=alt_text,upvotes=upvotes,downvotes=downvotes)
    db.session.add(image)
    db.session .commit()

def create_images(images):
    for image in images:
        newimage=Image(uri=image['uri'],alt_text=image['alt_text'],upvotes=image['upvote'],downvote=image['downvote'])
        db.session.add(newimage)
    db.session.commit()

def get_image_by_text(alt_text):
    return Image.query.filter_by(alt_text=alt_text).first()

def get_all_images():
    return Image.query.all()

def upvote_image(id):
    image=Image.query.filter_by(id=id).first()
    image.upvotes=image.upvotes+1
    db.session.commit()

def downvote_image(id):
    image=Image.query.filter_by(id=id).first()
    image.downvotes=image.downvotes+1
    db.session.commit()



