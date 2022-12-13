import unittest
import requests

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/login"

    data = {
        "name": "BoshMan",
        "password": "rokuz2001",
        "username": "Berkadam"
    }

    def test_3(self):
        resp = requests.post(self.URL, json=self.data)
        self.assertEqual(resp.status_code, 200)
        print("test 3 completed")

if __name__ == "__main__":
    tester = TestAPI()

    tester.test_3()
