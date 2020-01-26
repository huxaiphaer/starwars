import json
import unittest
import os
import sys

from run import app

sys.path.append(os.getcwd())


class BaseTestCase(unittest.TestCase):

    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config["TESTING"] = True
        return app

    def setUp(self):
        self.client = app.test_client(self)
        self.client.testing = True

    # def add_data(self):
    #     """
    #     add some mock data
    #     """
    #
    #     return self.client.post('/api/v1/starwars', json.dumps(
    #         dict(
    #             starships="", no_starship=""
    #         )
    #     ))

    def get_star_ships(self):
        """
        function to get star ships

        """
        return self.client.get('/api/v1/starwars')


