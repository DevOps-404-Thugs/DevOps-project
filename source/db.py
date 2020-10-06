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
