"""
This is the file containing all of the endpoints for our flask web app - iHomie
The endpoint called `endpoints` will return all available endpoints
"""

from flask import Flask, make_response, request, jsonify, render_template, url_for
from flask_restx import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from api_config import DB_URI
from db import get_user_info, login, signup
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
api = Api(app)
CORS(app)
parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')

app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)


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
    uid = db.Column(db.Integer, primary_key=True)
    user_name = db.StringField()
    user_pwd = db.StringField()

    def to_json(self):
        return {
            "uid": self.uid,
            "user_name": self.user_name,
            "user_pwd": self.user_pwd
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
        housing1 = Housing(housing_id=4,
                           name="867 Aagon Alley",
                           address="867 Aagon Ave")
        housing2 = Housing(housing_id=5,
                           name="438 Gu Yillage",
                           address="438 Dumb Street")
        housing1.save()
        housing2.save()
        user1 = User(uid="1",
                     user_name="tommy",
                     user_pwd="tandonCS")
        user2 = User(uid="2",
                     user_name="david",
                     user_pwd="tandonCS")
        user1.save()
        user2.save()
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


@api.route('/login')
class Login(Resource):
    """
    This class supports fetching a list of all housings
    """
    def get(self):
        """
        this method used for login
        """
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        return get_user_info(username) if login(username, password) else None


@api.route('/signup')
class Signup(Resource):
    """
    This class supports fetching a list of all housings
    """
    def put(self):
        """
        this method adds new user information
        """
        args = parser.parse_args()
        signup(args['username'], args['password'])
        return 'success'


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/ihomie")
def index_page():
    return render_template("index.html", flask_token="iHomie")


if __name__ == '__main__':
    app.run(debug=True)
