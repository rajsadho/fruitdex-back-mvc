from App.models import ( Image, User, Fruit, db )
from App.controllers import ( get_user_by_username, get_fruit_by_name )

def get_all_images_json():
    images=Image.query.all()
    if not images:
        return[]
    images=[images.toDict() for image in images]
    return images

def create_image(uri,alt_text,upvotes,downvotes):
    image=Image(uri=uri,alt_text=alt_text,upvotes=upvotes,downvotes=downvotes)
    db.session.add(image)
    db.session .commit()

def create_images(images):
    for image in images:
        user = get_user_by_username(image['username'])
        fruit = get_fruit_by_name(image['fruit'])
        newimage = Image(uri=image['uri'],alt_text=image['alt_text'])
        newimage.uploader = user
        newimage.fruit = fruit[0]
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



