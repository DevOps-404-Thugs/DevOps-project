"""
This is the file containing all of the endpoints for our flask web app - iHomie
The endpoint called `endpoints` will return all available endpoints
"""
from bson.objectid import ObjectId
from flask import Flask, make_response, request, jsonify, \
    flash, session
from flask_restx import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
from flask_wtf import FlaskForm
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, \
    logout_user, login_required, UserMixin
from flask_objectid_converter import ObjectIDConverter
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, \
    Email, EqualTo, ValidationError
from api_config import DB_URI
from pymongo import MongoClient
import datetime

app = Flask(__name__)
app.url_map.converters['objectid'] = ObjectIDConverter
app.config['SECRET_KEY'] = '68fe6951d932820ac5d2a0b5d352d77a'

api = Api(app)
CORS(app)
bcrypt = Bcrypt(app)

app.config["MONGODB_HOST"] = DB_URI
app.config['MONGODB_SETTINGS'] = {
    'db': 'API',
    'host': DB_URI
}
db = MongoEngine()
db.init_app(app)

client = MongoClient(DB_URI)
mydb = client["API"]
userCollection = mydb["user"]
housingCollection = mydb["housing"]

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        query = {"username": username.data}
        if userCollection.find(query).count() > 0:
            raise ValidationError('That username is taken. \
                Please choose a different one.')

    def validate_email(self, email):
        query = {"email": email.data}
        if userCollection.find(query).count() > 0:
            raise ValidationError('That email is taken. \
                Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.objects(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. \
                    Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.objects(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. \
                    Please choose a different one.')


class HousingForm(FlaskForm):
    name = StringField('Housing Name', validators=[DataRequired()])
    address = StringField('Housing Address', validators=[DataRequired()])
    submit = SubmitField('Post')


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


@login_manager.user_loader
def load_user(user_id):
    """
    loading user session for flask-login
    """
    return User.objects(pk=user_id).first()


@api.route('/db_populate')
class HousingDB(Resource):
    """
    This class will populate a demo initial housings database for housings
    """
    def post(self):
        """
        populate the initial database, returns 201 on success
        """
        user1 = User(
            username="tommy",
            email="tommy@gmail.com",
            password=bcrypt.generate_password_hash("123123").decode('utf-8'))
        user2 = User(
            username="david",
            email="david@gmail.com",
            password=bcrypt.generate_password_hash("123123").decode('utf-8'))
        user3 = User(
            username="sara",
            email="sara@gmail.com",
            password=bcrypt.generate_password_hash("123123").decode('utf-8'))
        user1.save()
        user2.save()
        user3.save()

        return make_response("", 201)


@api.route('/housings', methods=['GET', 'POST'])
class AllHousings(Resource):
    """
    This class will serve as GET and POST for all housings
    """
    def get(self):
        """
        The `get()` method will return all housing information
        """
        housings = []
        for housing in Housing.objects:
            housings.append(housing)
        return make_response(jsonify(housings), 200)

    @login_required
    def post(self):
        """
        The `post()` method will create new housing detail
        """
        content = request.form
        if content.get('name') is not None and content.get('address') is not None:
            housing = Housing(
                              name=content.get('name'),
                              address=content.get('address'),
                              date_posted=datetime.datetime.now(),
                              author_id=get_current_user_id(),
                              author_username=current_user.username)
            housing.save()
            return make_response("add successfully", 200)
        else:
            return make_response("parameter wrong", 400)


@api.route('/housings/<housing_id>', methods=['GET', 'PUT', 'DELETE'])
class HousingItem(Resource):
    """
    This class serves to get, put, and delete housing item
    """
    def get(self, housing_id):
        """
        GET/  return housing details of housing with _id
        """
        housing_obj = Housing.objects(_id=ObjectId(housing_id)).first()
        if housing_obj:
            return make_response(jsonify(housing_obj), 200)
        else:
            return make_response("parameter wrong", 404)

    @login_required
    def put(self, housing_id):
        """
        PUT/ update housing details of housing with _id, 204 on success
        """
        content = request.form
        housing = Housing.objects(_id=ObjectId(housing_id)).first()
        if housing.author_id != get_current_user_id():
            return make_response("no authority", 400)
        if content.get('name') is not None and content.get('address') is not None:
            housing.name = content.get('name')
            housing.address = content.get('address')
            housing.save()
            return make_response("update successfully", 200)
        else:
            return make_response("parameter wrong", 400)

    @login_required
    def delete(self, housing_id):
        """
        DELETE/ delete housing details of housing with _id
        """
        housing = Housing.objects(_id=ObjectId(housing_id)).first()
        if housing.author_id != get_current_user_id():
            return make_response("no authority", 400)
        delete_request = {"_id": ObjectId(housing_id)}
        housingCollection.delete_one(delete_request)
        return make_response("delete successfully", 200)


@api.route('/register')
class Register(Resource):
    """
    This class will serve as users creation
    """
    def post(self):
        """
        The `post()` method will create new username+pwd
        """
        content = request.form
        if current_user.is_authenticated:
            return make_response("authenticated wrong", 400)
        if User.objects(email=content.get('email')).first() is not None:
            return make_response("email has been registered", 400)
        if User.objects(email=content.get('username')).first() is not None:
            return make_response("username has been registered", 400)
        if content.get('username') is not None and content.get('password') \
                is not None and content.get('email') is not None:
            hashed_password = bcrypt.\
                generate_password_hash(content.get('password')).decode('utf-8')
            user = User(
                username=content.get('username'),
                email=content.get('email'),
                password=hashed_password
            )
            user.save()
            return make_response("register successfully", 200)
        else:
            return make_response("parameter wrong", 400)


@api.route('/login')
class Login(Resource):
    """
    This class will serve as users Login
    """
    def post(self):
        """
        The `post()` method will serve as users Login
        """
        content = request.form
        if current_user.is_authenticated:
            return make_response("authenticated wrong", 400)
        if content.get('email') is not None and content.get('password') is not None:
            check_user = User.objects(email=content.get('email')).first()
            if check_user:
                if bcrypt.check_password_hash(check_user["password"],
                                              content.get('password')):
                    session.permanent = True
                    app.permanent_session_lifetime = datetime.timedelta(minutes=30)
                    login_user(check_user)
                    return make_response("login successfully", 200)
                else:
                    return make_response("wrong password", 400)
            else:
                return make_response("need register", 400)
        else:
            return make_response("wrong parameters", 400)



@api.route('/logout')
class Logout(Resource):
    """
    This class will serve as users logout
    """
    def get(self):
        """
        The `get()` method will serve as users logout
        """
        logout_user()
        return make_response("logout successfully", 200)


@api.route('/account')
class Account(Resource):
    """
    This class serves to help user modify account information
    """
    def get(self):
        """
        GET/  return current user details
        """
        query = {"username": current_user.username,
                 "email": current_user.email}
        user = userCollection.find_one(query)
        if user:
            result = {}
            result['username'] = user.get('username')
            result['email'] = user.get('email')
            return make_response(jsonify(result), 200)
        else:
            return make_response("login timeout", 404)

    def put(self):
        """
        The `put()` method will modify current_user's email and password
        """
        content = request.form
        if content.get('username') is not None \
                and content.get('email') is not None:
            check_user = {"username": content.get('username'),
                          "email": content.get('email')}
            if userCollection.find(check_user).count() > 0:
                return make_response("user existed", 400)

            updated_user = {
                "$set": {
                        'username': content.get('username'),
                        'email': content.get('email')
                        }
                }
            query = {"username": current_user.username,
                     "email": current_user.email}
            userCollection.update_one(query, updated_user)
            current_user.username = content.get('username')
            current_user.email = content.get('email')
            return make_response("account updated successfully", 200)

        return make_response("wrong parameters", 400)


@login_required
def get_current_user_id():
    """
    retrieve user_id for current_user session
    """
    if current_user:
        query = {"username": current_user.username,
                 "email": current_user.email}
        user = userCollection.find_one(query)
        return str(user.get('_id'))


@app.route("/test")
def test():
    """
    developer test route
    """
    # find a cursor object
    print('current_user')
    print(type(current_user))
    user = userCollection.find_one({"username": "david"})
    print(type(user))

    return make_response("", 201)


def get_all_housings():
    """
    retrieve all housings for main page
    """
    housings = []
    for housing in housingCollection.find():
        housings.append(housing)
    return housings


if __name__ == '__main__':
    app.run(debug=True)
