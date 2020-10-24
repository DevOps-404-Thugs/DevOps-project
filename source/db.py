"""
This file will manage interactino with our data store.
At first, it will just contain stubs that return dummy data.
Gradually, we will fill in actual calls to our datastore.
"""

all_housings = {1: ["33 Bond Street", "www.housing.com"],
                3: ["474 Warrent Street", "www.housing.com"],
                2: ["Avalon Ave", "www.housing.com"],
                4: ["485 Clermont Ave", "www.housing.com"],
                5: ["110 Sex Street", "www.housing.com"],
                6: ["239 Hell Ave", "www.housing.com"]}

all_users = {"thommy": "123",
             "jack": "456"}


def get_user_info(username):
    """
    A function to return a detailed user with specified ID
    """
    return None if all_users.get(username) is None else username


def login(username, password):
    """
    A function to return a login status
    """
    token = ''.join(
        [value for key, value in all_users.items() if key == username])
    return True if password == token else False


def signup(username, password):
    """
    A function to signup
    """
    all_users[username] = password
