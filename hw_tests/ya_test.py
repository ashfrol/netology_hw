import unittest
import requests

class TestYaDisk(unittest.TestCase):

    def test_create_folder(self):
        params = {
            'path': 'test'
        }
        headers = {
            'Authorization': TOKEN
        }
        response = requests.put(DISC_URL, params=params, headers=headers)
        code = response.status_code
        self.assertEqual(code, 201)

    def test_check_folder(self):
        params = {
            'path': 'test'
        }
        headers = {
            'Authorization': TOKEN
        }
        response = requests.get(DISC_URL, params=params, headers=headers)
        code = response.status_code
        self.assertEqual(code, 200)

    def test_already_exists(self):
        params = {
            'path': 'test'
        }
        headers = {
            'Authorization': TOKEN
        }
        response = requests.put(DISC_URL, params=params, headers=headers)
        code = response.status_code
        self.assertEqual(code, 409)



