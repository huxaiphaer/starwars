from tests import BaseTestCase


class TestRequest(BaseTestCase):

    def test_home_route(self):
        """
        test the default route
        """
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

