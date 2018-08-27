from app import app
import unittest

class LoginTest(unittest.TestCase):

    def test_api_discount(self):
        tester = app.test_client(self)
        response = tester.post('/home', data=dict(btn_total_purchase='20'))
        print(response.data)
        self.assertEqual(response.status_code, 200)