from flask_login import UserMixin
from Housings import db

class User(db.Document, UserMixin):
    """
    This class defines the database for a generic user type for login/signup
    """
    meta = {'collection': 'user'}
    username = db.StringField()
    email = db.StringField()
    password = db.StringField()

    def to_json(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }