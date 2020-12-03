"""
This is the file containing all of the endpoints for our flask web app - iHomie
The endpoint called `endpoints` will return all available endpoints
"""
from bson.objectid import ObjectId
from flask import Flask, make_response, request, jsonify, \
    session, render_template
from flask_restx import Resource, Api
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, \
    logout_user, login_required
from flask_objectid_converter import ObjectIDConverter
from api_config import DB_URI
from pymongo import MongoClient
import datetime
from Housings import Housing, db
from Users import User

app = Flask(__name__)
app.url_map.converters['objectid'] = ObjectIDConverter
app.config['SECRET_KEY'] = '68fe6951d932820ac5d2a0b5d352d77a'

api = Api(app)
bcrypt = Bcrypt(app)

app.config["MONGODB_HOST"] = DB_URI
app.config['MONGODB_SETTINGS'] = {
    'db': 'API',
    'host': DB_URI
}

db.init_app(app)

client = MongoClient(DB_URI)
mydb = client["API"]
userCollection = mydb["user"]
housingCollection = mydb["housing"]

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


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
        content = request.json
        if content.get('name') is not None and \
                content.get('address') is not None:
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
        content = request.json
        housing = Housing.objects(_id=ObjectId(housing_id)).first()
        if housing.author_id != get_current_user_id():
            return make_response("no authority", 401)
        if content.get('name') is not None and \
                content.get('address') is not None:
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
        content = request.json
        if current_user.is_authenticated:
            return make_response("authenticated wrong", 400)
        if User.objects(email=content.get('email')).first() is not None:
            return make_response("email has been registered", 401)
        if User.objects(username=content.get('username')).first() is not None:
            return make_response("username has been registered", 402)
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
    This class will serve as users login
    """
    def get(self):
        """
        GET/ check whether a user is logged in
        """
        if current_user.is_authenticated:
            return make_response("a user has logged in", 200)
        return make_response("no current user logged in", 205)

    def post(self):
        """
        The `post()` method will serve as users Login
        """
        content = request.json
        if current_user.is_authenticated:
            return make_response("authenticated wrong", 400)
        if content.get('email') is not None and \
                content.get('password') is not None:
            check_user = User.objects(email=content.get('email')).first()
            if check_user:
                if bcrypt.check_password_hash(check_user["password"],
                                              content.get('password')):
                    session.permanent = True
                    app.permanent_session_lifetime = \
                        datetime.timedelta(minutes=30)
                    login_user(check_user)
                    return make_response("login successfully", 200)
                else:
                    return make_response("wrong password", 400)
            else:
                return make_response("need register", 401)
        else:
            return make_response("wrong parameters", 402)


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
    @login_required
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

    @login_required
    def put(self):
        """
        The `put()` method will modify current_user's email and password
        """
        content = request.json
        if content.get('username') is not None \
                and content.get('email') is not None:
            check_user = User.objects(
                username=content.get('username'),
                email=content.get('email')).first()
            if check_user:
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


@app.route("/ihomie")
def my_index():
    return render_template("index.html", flask_token="Hello world")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000, use_reloader=True)
