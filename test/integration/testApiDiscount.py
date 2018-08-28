from app import app
import unittest
import json

class DiscountApiTest(unittest.TestCase):

    def test_api_discount_purchase_is_25__and_discount_is_20(self):
        tester = app.test_client(self)
        response = tester.post('/home', data=dict(btn_total_purchase='25'))

        result_expect = [{'total_discount': 20}]
        result_actual = json.loads(response.data.decode('utf-8'))

        self.assertEqual(result_actual, {'discount': result_expect})

        self.assertEqual(response.status_code, 200)