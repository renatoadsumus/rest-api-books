from api import app
import unittest
import json

class TestApp(unittest.TestCase):

    def test_app_is_alive_app_page(self):
        tester = app.test_client(self)
        response = tester.get('/app-name/api/v0.1/tasks')
        data = json.loads(response.data.decode('utf-8'))
        print(response.data)
        tasks = [
            {
                'id': 1,
                'task': 'this is first task'
            },
            {
                'id': 2,
                'task': 'this is another task'
            }
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'tasks': tasks})


if __name__ == '__main__':
    unittest.main()