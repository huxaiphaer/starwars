from tests import BaseTestCase


class TestRequest(BaseTestCase):

    def test_star_ships_returned_successfully(self):

        result = self.client('api/v1/starwars')
        self.assertEqual(result.status_code, 200)

    def test_home_route(self):

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
