"""
This is the file containing all of the endpoints for our flask web app - iHomie
The endpoint called `endpoints` will return all available endpoints
"""

from flask import Flask, make_response, request, jsonify
from flask_restx import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
from api_config import DB_URI
from db import get_user_info, login, signup

app = Flask(__name__)
api = Api(app)
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
    user_id = db.IntField()
    user_pwd = db.StringField()

    def to_json(self):
        return {
            "user_id": self.user_id,
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
        return make_response("", 201)


@api.route('/housings')
class AllHousings(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system
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
    def get(self):
        """
        First endpoint to bridge running server
        """
        return {'hello': 'world'}


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
        return ''


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


if __name__ == '__main__':
    app.run(debug=True)
