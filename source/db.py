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


def get_all_housing():
    """
    A function to return all housings in the data store.
    """
    return all_housings


def get_housing_info(id):
    """
    A function to return a detailed housing with specified ID
    """
    return None if all_housings.get(id) is None else all_housings.get(id)


def get_housing_info_link(id):
    """
    a function to return the web link for a housing with specified ID
    """
    return None if all_housings.get(id)is None or \
        len(all_housings.get(id)) < 2 else all_housings.get(id)[1]


def add_housing_info(address, link):
    """
    a function to add a housing
    """
    id = max(all_housings.keys()) + 1
    all_housings[id] = [address, link]


def update_housing_info(id, address):
    """
    a function to update a housing address
    """
    if all_housings.get(id) is not None:
        all_housings.get(id)[0] = address


def delete_housing_info(id):
    """
    a function to delete a housing
    """
    if all_housings.get(id) is not None:
        del(all_housings[id])


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
