from flask_mongoengine import MongoEngine

db = MongoEngine()

class Housing(db.Document):
    """
    This class defines the database for a generic housing type
    """
    meta = {'collection': 'housing'}
    _id = db.ObjectIdField()
    name = db.StringField()
    address = db.StringField()
    date_posted = db.DateTimeField()
    author_id = db.StringField()
    author_username = db.StringField()

    def to_json(self):
        return {
            "name": self.name,
            "address": self.address,
            "author_id": self.author_id,
            "author_username": db.StringField()
        }


