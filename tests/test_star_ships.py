from tests import BaseTestCase


class TestRequest(BaseTestCase):

    def test_star_ships_returned_successfully(self):
        with self.client:
            # self.add_data()
            res = self.get_star_ships()
            # print(res)
            self.assertEqual(res.statuscode, 200)
