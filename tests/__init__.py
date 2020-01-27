import json
import unittest
import os
import sys
from http import server

import fakeredis
import redis

from config.config import app_config
from run import app, paginate_requested_data, insert_data

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
        self.server = fakeredis.FakeServer()
        self.fake_redis_db = fakeredis.FakeStrictRedis(server=self.server)
        self.task = paginate_requested_data.apply_async()
        self.results = self.task.get()

    def add_data(self, name, hyper_drive_rating):
        """
        add some mock data
        """
        return insert_data(self.fake_redis_db, name, hyper_drive_rating)

    def get_test_state(self):
        """
        get test state
        """
        return self.task.state

