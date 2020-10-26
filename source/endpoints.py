"""
This is the file containing all of the endpoints for our flask web app - iHomie
The endpoint called `endpoints` will return all available endpoints
"""

from flask import Flask, make_response, request, jsonify, render_template, url_for, flash, redirect
from flask_restx import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
from flask_wtf import FlaskForm
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_login import UserMixin
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from api_config import DB_URI
from db import get_user_info, login, signup
# from forms import RegistrationForm, LoginForm
from pymongo import MongoClient

app = Flask(__name__)
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
userCollection = mydb["tempuser"]

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
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        query = {"username": username.data}
        if userCollection.find(query).count() > 0:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        query = {"email": email.data}
        if userCollection.find(query).count() > 0:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


@app.route("/test")
def test():
    query = {"username": "david"}
    user = userCollection.find(query) # <pymongo.cursor.Cursor object at 0x10eb0eed0>
    print('user: ')
    print(user) 
    # print('password: ')
    # print(user["password"])
    # print('each doc in docs -------')
    # for doc in docs:
    #     print(doc)

    print(userCollection.find(query).count())
    return make_response("", 201)


class Housing(db.Document):
    """
    This class defines the database for a generic housing type
    """
    housing_id = db.IntField()
    name = db.StringField()
    address = db.StringField()

    def to_json(self):
        return {
            "housing_id": self.housing_id,
            "name": self.name,
            "address": self.address
        }


class User(db.Document):
    """
    This class defines the database for a generic user type for login/signup
    """
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
    return Tempuser.objects(pk=user_id).first()
    # query = {"id": user_id}
    # return userCollection.find_one(query)
    # return User.query.get(int(user_id))


class Tempuser(db.Document, UserMixin):
    """
    This class defines the database for a generic user type for login/signup
    """
    meta = {'collection': 'tempuser'}
    # uid = db.IntField()
    username = db.StringField()
    email = db.StringField()
    password = db.StringField()

    def to_json(self):
        return {
            # "uid": self.self.uid,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }


@api.route('/db_populate')
class HousingDB(Resource):
    """
    This class will populate a demo initial housings database for housings
    """
    def post(self):
        """
        populate the initial database, returns 201 on success
        """
        # housing1 = Housing(housing_id=4,
        #                    name="867 Aagon Alley",
        #                    address="867 Aagon Ave")
        # housing2 = Housing(housing_id=5,
        #                    name="438 Gu Yillage",
        #                    address="438 Dumb Street")
        # housing1.save()
        # housing2.save()

        tempuser1 =  Tempuser(uid=1,
                     username="tommy",
                     email="tommy@gmail.com",
                     password="123123")
        tempuser2 =  Tempuser(uid=2,
             username="david",
             email="david@gmail.com",
             password="123123")
        tempuser3 =  Tempuser(uid=3,
             username="sara",
             email="sara@gmail.com",
             password="123123")
        tempuser1.save()
        tempuser2.save()
        tempuser3.save()
        return make_response("", 201)


@api.route('/housings')
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

    def post(self):
        """
        The `post()` method will create new housing detail
        """
        content = request.json
        housing = Housing(housing_id=content['housing_id'],
                          name=content['name'],
                          address=content['address'])
        housing.save()
        return make_response("", 201)


@api.route('/housings/<housing_id>', methods=['GET', 'PUT', 'DELETE'])
class HousingItem(Resource):
    """
    This class serves to get, put, and delete housing item
    """
    def get(self, housing_id):
        """
        GET/  return housing details of housing with _id
        """
        housing_obj = Housing.objects(housing_id=housing_id).first()
        if housing_obj:
            return make_response(jsonify(housing_obj.to_json()), 200)
        else:
            return make_response("", 404)

    def put(self, housing_id):
        """
        PUT/ update housing details of housing with _id, 204 on success
        """
        content = request.json
        housing_obj = Housing.objects(housing_id=housing_id).first()
        housing_obj.update(name=content['name'], address=content['address'])
        return make_response("", 204)

    def delete(self, housing_id):
        """
        DELETE/ delete housing details of housing with _id
        """
        housing_obj = Housing.objects(housing_id=housing_id).first()
        housing_obj.delete()
        return make_response("", 204)


@api.route('/hello')
class HelloWorld(Resource):
    @app.route("/greeting")
    def greeting():
        """
        set for dummy app route
        """
        test_housings = [{'housing_id': '1',
                          'name': '123 Great',
                          'address': '123 Great Ave',
                          'content': 'Renting now, $1500 per month'},
                          {'housing_id': '2',
                          'name': '234 Great',
                          'address': '234 Great Ave',
                          'content': 'Renting now, $2300 per month'},
                          ]
        return render_template('home.html', housings=test_housings)

    def get(self):
        """
        First endpoint to bridge running server
        """
        return "{'hello': 'world'}"


@api.route('/users')
class AllUsers(Resource):
    """
    This class will serve as users GET and creation
    """
    def get(self):
        """
        The `get()` method will return all users username+pwd
        """
        users = []
        for user in User.objects:
            users.append(user)
        return make_response(jsonify(users), 200)

    def post(self):
        """
        The `post()` method will create new username+pwd
        """
        content = request.json
        user = User(user_name=content['user_name'],
                    user_pwd=content['user_pwd']
                    )
        user.save()
        return make_response("", 201)


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system
    """
    def get(self):
        """
        The `get()` method will return a list of endpoitns along with
        documentation on them
        """
        return {'end': 'point'}


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Tempuser(username=form.username.data, email=form.email.data, password=hashed_password)
        user.save()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        check_user = Tempuser.objects(email=form.email.data).first()
        if check_user and bcrypt.check_password_hash(check_user["password"], form.password.data):
            login_user(check_user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/home")
def home():
    housings = [{'housing_id': 4,
                 'name': '867 Local Aagon Alley',
                 'address': '867 Local Aagon Ave'}, 
                 {'housing_id': 5,
                 'name': '438 Local Gu Yillage',
                 'address': '438 Local Dumb Street'}
                 ]
    return render_template("home.html", housings=housings)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


if __name__ == '__main__':
    app.run(debug=True)
