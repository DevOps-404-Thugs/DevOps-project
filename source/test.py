import json
import unittest

from endpoints import app


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

    def test_get_all_housings(self):
        # test the method getting all housing info
        response = self.client.get("/housings", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        info = resp[0].get("address")
        self.assertEqual(info, "857 Aagon Ave")

    def test_post_housing_info(self):
        response = self.client.get("/housings", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        length = len(resp)
        id = resp[length - 1]['housing_id'] + 1
        info = {'housing_id': id, 'name': '343 Gold Ave',
                'address': '343 Gold Street'}

        response = self.client.post("/housings", data=info)
        resp = response.status_code
        self.assertEqual(resp, 201)

        response = self.client.get("/housings", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        info = resp[id - 1].get("address")
        self.assertEqual(info, "343 Gold Street")


class HousingItemTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_housing_item(self):
        # test the method getting the details of housing
        response = self.client.get("/housings/1", data={})
        self.assertEqual(response.status_code, 200)

        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp.get("address"), "857 Aagon Ave")

    def test_put_housing_item(self):
        info = {'name': '342 Gold Ave', 'address': '342 Gold Street'}
        response = self.client.put("/housings/4", data=info)
        self.assertEqual(response.status_code, 204)

        response = self.client.get("/housings/4", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp.get("address"), "342 Gold Street")

        info = {'name': '343 Gold Ave', 'address': '343 Gold Street'}
        response = self.client.put("/housings/4", data=info)
        self.assertEqual(response.status_code, 204)

        response = self.client.get("/housings/4", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp.get("address"), "343 Gold Street")

    def test_delete_housing_item(self):
        response = self.client.get("/housings", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        length = len(resp)
        id = resp[length - 1]['housing_id']
        if (length > 0):
            response = self.client.delete("/housings/%s" % id)
            self.assertEqual(response.status_code, 204)


class AllUsersTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_all_users(self):
        # test the method getting the details of housing
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)

    def test_post_user_info(self):
        info = {'user_name': 'betty', 'user_pwd': '343'}
        response = self.client.post("/users", data=info)
        self.assertEqual(response.status_code, 201)

        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        resp_json = response.data
        resp = json.loads(resp_json)
        length = len(resp)
        self.assertEqual('betty', resp[length - 1].get('user_name'))


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_login(self):
        # test the method loggin in
        response = self.client.get("/login",
                                   data={'user_name': 'thommy',
                                         'user_pwd': '123'})
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
                                   data={'user_name': 'betty',
                                         'user_pwd': '456'})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp, "success")

        # test whether sign up is a success
        response = self.client.get("/login",
                                   data={'user_name': 'betty',
                                         'user_pwd': '456'})
        resp_json = response.data
        resp = json.loads(resp_json)
        self.assertEqual(resp, "betty")


class IndexPageTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_page(self):
        # test the method getting endpoints
        response = self.client.get("/ihomie")
        self.assertEqual(response.status_code, 200)


class HousingDBTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_post_info(self):
        response = self.client.post("/db_populate")
        self.assertEqual(response.status_code, 201)

        response = self.client.get("/housings", data={})
        resp_json = response.data
        resp = json.loads(resp_json)
        info = resp[3].get("address")
        self.assertEqual(info, "867 Aagon Ave")


if __name__ == '__main__':
    unittest.main()
