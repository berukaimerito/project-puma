
import unittest
import requests

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/register"

    data = {
        "name": "BoshMan",
        "password": "rokuz2001",
        "username": "Berkadam",
        "mail": "galengosse@gmail.com",
        "cell": "572348061"
    }

    def test_2(self):
        resp = requests.post(self.URL, json=self.data)
        self.assertEqual(resp.status_code, 201)
        print("test 2 completed")

if __name__ == "__main__":
    tester = TestAPI()

    tester.test_2()
