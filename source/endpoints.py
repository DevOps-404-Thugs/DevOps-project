"""
This is the file containing all of the endpoints for our flask web app - iHomie
The endpoint called `endpoints` will return all available endpoints
"""

from flask import Flask
from flask_restx import Resource, Api, reqparse
from db import get_all_housing, get_housing_info, get_housing_info_link, get_user_info, login, add_housing_info,\
    delete_housing_info, update_housing_info, signup

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        """
        First endpoint to bridge running server
        """
        return {'hello': 'world'}


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


@api.route('/housings')
class Housings(Resource):
    """
    This class supports fetching a list of all housings
    """
    def get(self):
        """
        this method returns all housings
        """
        return get_all_housing()


@api.route('/housings/<int:id>')
@api.response(404, 'Housing not found.')
class HousingItem(Resource):
    """
    This class serves to get, put, and delete housing item
    """
    def get(self, id):
        """
        Returns details of a housing.
        """
        return get_housing_info(id)

    def get_weblink(self, id):
        """
        Returns weblink of a housing.
        """
        return get_housing_info_link(id)

@api.route('/login')
@api.response(404, 'User not found.')
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

@api.route('/add/<string:address>+<string:link>')
class AddHouseInfo(Resource):
    """
    This class supports fetching a list of all housings
    """
    def post(self, address, link):
        """
        this method adds housing information
        """
        add_housing_info(address, link)
        return 'success'

@api.route('/update/<int:id>+<string:address>')
class UpdateHouseInfo(Resource):
    """
    This class supports fetching a list of all housings
    """
    def post(self, id, address):
        """
        this method updates housing address
        """
        update_housing_info(id, address)
        return 'success'

@api.route('/delete/<int:id>')
class DeleteHouseInfo(Resource):
    """
    This class supports fetching a list of all housings
    """
    def delete(self, id):
        """
        this method deletes housing link
        """
        delete_housing_info(id)
        return 'success'

if __name__ == '__main__':
    app.run(debug=True)
