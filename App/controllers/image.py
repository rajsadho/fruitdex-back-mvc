from App.models import ( Image, User, Fruit, db )
from App.controllers import ( get_user_by_username, get_fruit_by_name )
from flask_jwt import current_identity

def get_all_images_json():
    images=Image.query.all()
    if not images:
        return[]
    images=[image.toDict() for image in images]
    return images

def get_image_by_id_json(id):
    image=Image.query.filter_by(id=id).first()
    if not image:
        return None
    return image.toDict()

def get_images_by_user_id_json(user_id):
    images=Image.query.filter_by(uploader_id=user_id).all()
    if not images:
        return[]
    images=[image.toDict() for image in images]
    return images

def get_images_by_fruit_id_json(fruit_id):
    images=Image.query.filter_by(fruit_id=fruit_id).all()
    if not images:
        return[]
    images=[image.toDict() for image in images]
    return images

def create_image(args):
    fruit = Fruit.query.filter_by(id=args['fruit_id']).first()
    image=Image(uri=args['uri'],alt_text=args['alt_text'])
    image.fruit = fruit
    image.uploader = current_identity
    db.session.add(image)
    db.session.commit()

def create_images(images):
    for image in images:
        user = get_user_by_username(image['username'])
        fruit = get_fruit_by_name(image['fruit'])
        newimage = Image(uri=image['uri'],alt_text=image['alt_text'])
        user.images.append(newimage)
        fruit[0].images.append(newimage)
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



