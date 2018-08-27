from app import app
import unittest

class LoginTest(unittest.TestCase):

    def test_app_is_alive_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/')
        print(response.data)
        self.assertEqual(response.status_code,200)

    def test_app_correct_password(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(username='admin', password='admin'))
        self.assertEqual(response.status_code,302)

    def test_app_wrong_password(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(username='admin', password='wrong'))
        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()

