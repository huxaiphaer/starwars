import unittest
import fakeredis

from config import create_app, app_config
from run import insert_data, paginate_requested_data, app, make_request


class TestStar(unittest.TestCase):

    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.app = create_app('testing')
        self.server = fakeredis.FakeServer()
        self.fake_redis_db = fakeredis.FakeStrictRedis(server=self.server)
        self.client = app.test_client(self)

    def test_add_data(self):
        """
        test when we add data to redis
        """
        res = insert_data(self.fake_redis_db, "huxy", "2.1")
        self.assertIsNotNone(res)

    def test_default_route(self):

        res = self.client.get('/')
        self.assertIsNotNone(res)

    def test_paginated_data(self):

        res = make_request('https://swapi.co/api/starships/', self.fake_redis_db)
        self.assertIsNotNone(res)

    def test_get_starwars_endpoint(self):

        res = self.client.get('/api/v1/starwars')
        self.assertIsNotNone(res)

