from App.models import ( FruitName, db )

def get_all_fruit_names_json():
    names=FruitName.query.all()
    if not names:
        return []
    names=[name.toDict() for name in names]
    return names

def create_fruit_name(name,name_type):
    fruit=FruitName(name=name,name_type=name_type)
    db.session.add(fruit)
    db.session.commit()

def create_fruit_names(fruits):
    for fruit in fruits:
        newfruit=FruitName(name=fruit['name'],name_type=fruit['name_type'])
        db.session.add(newfruit)
    db.session.commit()

def get_fruit_by_name(name):
    return FruitName.query.filter_by(name=name).first()

def get_fruit_by_nametype(name_type):
    return FruitName.query.filter_by(name_type=name_type).first()