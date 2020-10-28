"""
This is the file containing all of the endpoints for our flask web app - iHomie
The endpoint called `endpoints` will return all available endpoints
"""

from flask import Flask, make_response, request, jsonify, \
    render_template, url_for, flash, redirect, abort
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
userCollection = mydb["tempuser"]
housingCollection = mydb["temphousing"]

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
            user = Tempuser.objects(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. \
                    Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Tempuser.objects(email=email.data).first()
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


class Tempuser(db.Document, UserMixin):
    """
    This class defines the database for a generic user type for login/signup
    """
    meta = {'collection': 'tempuser'}
    username = db.StringField()
    email = db.StringField()
    password = db.StringField()

    def to_json(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }


class Temphousing(db.Document):
    """
    This class defines the database for a generic housing type
    """
    meta = {'collection': 'temphousing'}
    name = db.StringField()
    address = db.StringField()
    date_posted = db.DateTimeField()
    author_id = db.StringField()
    author_username = db.StringField()

    def to_json(self):
        return {
            "housing_id": self.housing_id,
            "name": self.name,
            "address": self.address,
            "author_id": self.author_id,
            "author_username": db.StringField()
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
        tempuser1 = Tempuser(
            username="tommy",
            email="tommy@gmail.com",
            password="123123")
        tempuser2 = Tempuser(
            username="david",
            email="david@gmail.com",
            password="123123")
        tempuser3 = Tempuser(
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


@api.route('/greeting')
class HelloWorld(Resource):
    @app.route("/greeting")
    def greeting():
        """
        set for dummy app route
        """
        return render_template('home.html', housings=get_all_housings())

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


@app.route("/housing/new", methods=['GET', 'POST'])
@login_required
def new_housing():
    form = HousingForm()
    if form.validate_on_submit():
        housing = Temphousing(name=form.name.data,
                              address=form.address.data,
                              date_posted=datetime.datetime.now(),
                              author_id=get_current_user_id(),
                              author_username=current_user.username)
        housing.save()
        flash('Your housing has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_housing.html', title='New Housing',
                           form=form, legend='New Housing')


@app.route("/housing/<objectid:housing_id>")
def post(housing_id):
    housing = Temphousing.objects(pk=housing_id).first()
    return render_template(
                            'housing.html',
                            name=housing.name,
                            address=housing.address,
                            housing_id=housing_id,
                            housing=housing,
                            current_user_id=get_current_user_id()
                            )


@app.route("/housing/<objectid:housing_id>/update", methods=['GET', 'POST'])
@login_required
def update_housing(housing_id):
    housing = Temphousing.objects(pk=housing_id).first()
    if housing.author_id != get_current_user_id():
        abort(403)
    form = HousingForm()
    if form.validate_on_submit():
        housing.name = form.name.data
        housing.address = form.address.data
        housing.save()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', housing_id=housing_id))
    elif request.method == 'GET':
        form.name.data = housing.name
        form.address.data = housing.address

    return render_template('create_housing.html', title='Update Housing',
                           form=form, legend='Update Housing')


@app.route("/housing/<objectid:housing_id>/delete", methods=['POST'])
@login_required
def delete_housing(housing_id):
    housing = Temphousing.objects(pk=housing_id).first()
    if housing.author_id != get_current_user_id():
        abort(403)
    delete_request = {"_id": housing_id}
    housingCollection.delete_one(delete_request)
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data). \
            decode('utf-8')
        user = Tempuser(
                        username=form.username.data,
                        email=form.email.data,
                        password=hashed_password
                        )
        user.save()
        flash('Your account has been created! \
            You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        check_user = Tempuser.objects(email=form.email.data).first()
        if check_user:
            if bcrypt.check_password_hash(check_user["password"],
                                          form.password.data):
                login_user(check_user)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page \
                    else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. \
                Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/home")
def home():
    return render_template("home.html", housings=get_all_housings())


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    updated_user = {
                    "$set": {
                            'username': form.username.data,
                            'email': form.email.data
                            }
                    }
    if form.validate_on_submit():
        query = {"username": current_user.username,
                 "email": current_user.email}
        userCollection.update_one(query, updated_user)
        changed_param = "nothing"
        if current_user.username != form.username.data \
                and current_user.email != form.email.data:
            changed_param = "account username and email"
        elif current_user.username != form.username.data:
            changed_param = "username"
        elif current_user.email != form.email.data:
            changed_param = "email"
        else:
            # safely exit without update
            flash('Please use a different username or \
                email than your current account', 'warning')
            return redirect(url_for('account'))
        current_user.username = form.username.data
        current_user.email = form.email.data
        flash('Your %s has been updated!' % changed_param, 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', title='Account', form=form)


@login_required
def get_current_user_id():
    if current_user:
        query = {"username": current_user.username,
                 "email": current_user.email}
        user = userCollection.find_one(query)
        return str(user.get('_id'))


@app.route("/test")
def test():
    # find a cursor object
    user = userCollection.find_one({"username": "david"})
    print(user.username)
    return make_response("", 201)


def get_all_housings():
    housings = []
    for housing in housingCollection.find():
        housings.append(housing)
    return housings


if __name__ == '__main__':
    app.run(debug=True)
