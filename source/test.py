import unittest
import json
from source.endpoints import app

class HelloWorldTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_hello_world(self):
        response = self.client.get("/hello", data={})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("hello", resp_dict)
        hello = resp_dict.get("hello")
        self.assertEqual(hello, "world")

class EndpointsTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_endpoints(self):
        response = self.client.get("/endpoints", data={})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("end", resp_dict)
        end = resp_dict.get("end")
        self.assertEqual(end, "point")

class HousingsInfoTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_housings(self):
        response = self.client.get("/housings", data={})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("1", resp_dict)
        info = resp_dict.get("1")
        self.assertEqual(info[1], "www.housing.com")

class HousingInfoTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_housing_item(self):
        response = self.client.get("/housings/1", data={})
        resp_json = response.data
        resp_array = json.loads(resp_json)
        self.assertEqual(resp_array[0], "33 Bond Street")

    def test_housing_link(self):
        pass

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_login(self):
        response = self.client.get("/login", data={'username' : 'thommy', 'password' : '123'})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp, "thommy")

class SignupTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_signup(self):
        response = self.client.put("/signup", data={'username' : 'thommy', 'password' : '123'})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp, "success")



if __name__ == '__main__':
    unittest.main()
