from App.models import ( Fruit, FruitTag, FruitName, Tag, db )
from App.controllers import ( create_fruit_names_list, get_tag_by_value )


def create_fruit(wiki_uri,names):
    fruit=Fruit(wiki_uri=wiki_uri,names=names)
    db.session.add(fruit)
    db.commit()

def create_fruits(fruits):
    for fruit in fruits:
        names = create_fruit_names_list(fruit['names'])
        newfruit=Fruit(wiki_uri=fruit['wiki_uri'],names=names)
        
        for tag in fruit['tags']:
            tag = get_tag_by_value(tag['value'])
            fruit_tag = FruitTag()
            fruit_tag.tag = tag
            newfruit.tags.append(fruit_tag)
            db.session.add(fruit_tag)
            db.session.commit()

        db.session.add(newfruit)
    db.session.commit()

def add_fruit_image(fruit, image):
    fruit.images.append(image)
    db.commit()


def get_all_fruits_json():
    fruits=Fruit.query.all()
    if not fruits:
        return []
    fruits=[fruit.toDict() for fruit in fruits]
    return fruits

def get_all_fruits():
    return Fruit.query.all()

def get_fruit_by_name(name):
    return db.session.query(Fruit).\
        join(FruitName, Fruit.id == FruitName.fruit_id).\
        filter(FruitName.name == name).\
        all()

def get_fruit_by_tag(tag):
    return db.session.query(Fruit).\
        join(FruitTag, Fruit.id == FruitTag.fruit_id).\
        join(Tag, Tag.id == FruitTag.tag_id).\
        filter(Tag.value == tag).\
        all()



