import json
import unittest
import os
import sys

import fakeredis
import redis

from config.config import app_config
from run import app

sys.path.append(os.getcwd())


class BaseTestCase(unittest.TestCase):

    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config['testing'])
        return app

    def setUp(self):
        self.client = app.test_client(self)
        self.client.testing = True
        self.redis_db = fakeredis.FakeStrictRedis()

    def add_data(self, name, hyper_drive_rating):
        """
        add some mock data
        """
        self.redis_db.hset('test_data', name, hyper_drive_rating)

    def get_star_ships(self):
        """
        function to get star ships

        """
        return self.client.get('/api/v1/starwars')

