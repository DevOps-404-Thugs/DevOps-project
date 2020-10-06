"""
This is the file containing all of the endpoints for our flask web app - iHomie
The endpoint called `endpoints` will return all available endpoints
"""

from flask import Flask
from flask_restx import Resource, Api
from db import get_all_housing, get_housing_info, get_housing_info_link

app = Flask(__name__)
api = Api(app)


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


if __name__ == '__main__':
    app.run(debug=True)
