import unittest
import fakeredis

from run import insert_data, paginate_requested_data


class TestStar(unittest.TestCase):

    def setUp(self):
        self.server = fakeredis.FakeServer()
        self.fake_redis_db = fakeredis.FakeStrictRedis(server=self.server)

    def test_add_data(self):
        """
        test when we add data to redis
        """
        res = insert_data(self.fake_redis_db, "huxy", "2.1")
        self.assertIsNotNone(res)

