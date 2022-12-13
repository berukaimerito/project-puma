import unittest
import requests

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/homepage"

    def test_1(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 1)
        print("test 1 completed")


if __name__ == "__main__":
    tester = TestAPI()

    tester.test_1()


