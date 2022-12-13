import unittest
import requests


class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/homepage"

    # data = {
    #     "name": "BoshMan",
    #     "password": "rokuz2001",
    #     "username": "Berkadam"
    # }

    # expected_result = {
    #     "message": "user has been created successfully."
    # }

    # def test_4_1(self):
    #     resp = requests.post(self.URL, json=self.data)
    #     self.assertEqual(resp.status_code, 200)
    #     print("test 4_1 completed")

    def test_4_1(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()), 1)
        print("test 4_1 completed")


    def test_4_2(self):
        resp = requests.get(self.URL + '/register')
        self.assertEqual(resp.status_code, 200)
        # self.assertEqual(resp.json(), self.expected_result)
        print("test 4_2 completed")


if __name__ == "__main__":
    tester = TestAPI()

    tester.test_4_1()
    tester.test_4_2()
