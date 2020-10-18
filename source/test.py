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

    def test_hello_world(self):
        response = self.client.get("/endpoints", data={})
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        self.assertIn("end", resp_dict)
        end = resp_dict.get("end")
        self.assertEqual(end, "point")

if __name__ == '__main__':
    unittest.main()
