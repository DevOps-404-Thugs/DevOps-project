import json
import unittest
from endpoints import app


class HousingsTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()
        info = {"username": "betty", "password": "123456",
                "email": "zbn@ihomie.com"}
        self.client.post("/login", json=info)

    def tearDown(self):
        self.client.get("/logout")

    def test_1_get_all_housings(self):
        response = self.client.get("/housings")
        self.assertEqual(response.status_code, 200)

    def test_2_post_housing_info(self):
        info = {'name': 'Avalon FG',
                'address': '343 Gold Street'}
        response = self.client.post("/housings", json=info)

        self.assertEqual(response.status_code, 200)

    def test_3_get_housing_item(self):
        response = self.client.get("/housings")
        resp_json = json.loads(response.data)
        housing_id = resp_json[len(resp_json) - 1]['_id']['$oid']
        response = self.client.get("/housings/" + housing_id)
        self.assertEqual(response.status_code, 200)

    def test_4_update_housing_item(self):
        response = self.client.get("/housings")
        resp_json = json.loads(response.data)
        housing_id = resp_json[len(resp_json) - 1]['_id']['$oid']
        info = {'name': 'Avalon FG',
                'address': '343 Gold Street'}
        response = self.client.put("/housings/" + housing_id, json=info)
        self.assertEqual(response.status_code, 200)

    def test_5_delete_housing_item(self):
        response = self.client.get("/housings")
        resp_json = json.loads(response.data)
        housing_id = resp_json[len(resp_json) - 1]['_id']['$oid']
        response = self.client.delete("/housings/" + housing_id)
        self.assertEqual(response.status_code, 200)


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()
        info = {"username": "betty", "password": "123456",
                "email": "zbn@ihomie.com"}
        self.client.post("/login", json=info)

    def tearDown(self):
        self.client.get("/logout")

    def test_1_get_account_info(self):
        response = self.client.get("/account")
        self.assertEqual(response.status_code, 200)

    def test_2_update_account_info(self):
        info = {"username": "betty-ut",
                "email": "zbn@ihomie.com"}
        response = self.client.get("/account", json=info)
        self.assertEqual(response.status_code, 200)

        info = {"username": "betty",
                "email": "zbn@ihomie.com"}
        response = self.client.get("/account", json=info)
        self.assertEqual(response.status_code, 200)


class LogTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_login_status(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 205)

    def test_1_login(self):
        # test the method loggin in
        info = {"username": "betty", "password": "123456",
                "email": "zbn@ihomie.com"}
        response = self.client.post("/login", json=info)
        self.assertEqual(response.status_code, 200)

    def test_2_logout(self):
        # test the method loggin in
        response = self.client.get("/logout")
        self.assertEqual(response.status_code, 200)


class SignupTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_signup(self):
        # test the method signing up
        info = {"username": "betty", "password": "123456",
                "email": "zbn@ihomie.com"}
        response = self.client.post("/register",
                                    json=info)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
