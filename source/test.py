import unittest
import json
from source.endpoints import app


class HelloWorldTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_hello_world(self):
        # # test the method hello world
        response = self.client.get("/hello", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertIn("hello", resp)
        hello = resp.get("hello")
        self.assertEqual(hello, "world")


class EndpointsTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_endpoints(self):
        # test the method getting endpoints
        response = self.client.get("/endpoints", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertIn("end", resp)
        end = resp.get("end")
        self.assertEqual(end, "point")


class HousingsTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_housings(self):
        # test the method getting all housing info
        response = self.client.get("/housings", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertIn("1", resp)
        info = resp.get("1")
        self.assertEqual(info[1], "www.housing.com")


class HousingItemTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_housing_item(self):
        # test the method getting the details of housing
        response = self.client.get("/housings/1", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp[0], "33 Bond Street")

    def test_housing_link(self):
        pass


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_login(self):
        # test the method loggin in
        response = self.client.get("/login",
                                   data={'username': 'tommy',
                                         'password': '123'})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp, "thommy")


class SignupTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_signup(self):
        # test the method signing up
        response = self.client.put("/signup",
                                   data={'username': 'betty',
                                         'password': '456'})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp, "success")

        # test whether sign up is a success
        response = self.client.get("/login",
                                   data={'username': 'betty',
                                         'password': '456'})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp, "betty")


class AddHouseInfoTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_add_house_info(self):
        # test the method adding house information
        response = self.client.post(
            "/add/343 Gold Street+www.housing.com", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp, "success")

        # test whether the adding is a success
        response = self.client.get("/housings", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        info = resp.get(str(len(resp)))
        self.assertEqual(info[0], "343 Gold Street")


class UpdateHouseInfo(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_update_house_info(self):
        # test the method updating house information
        response = self.client.post("/update/1+343 Gold Street", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp, "success")

        # test whether the updating is a success
        response = self.client.get("/housings/1", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp[0], "343 Gold Street")


class DeleteHouseInfo(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_delete_house_info(self):
        # test the method deleting house information
        response = self.client.delete("/delete/2", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp, "success")

        # test whether the deleting is a success
        response = self.client.get("/housings/2", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertIsNone(resp)


if __name__ == '__main__':
    unittest.main()
