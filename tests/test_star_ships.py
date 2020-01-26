from tests import BaseTestCase


class TestRequest(BaseTestCase):

    def test_home_route(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
