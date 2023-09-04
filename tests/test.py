from unittest import TestCase, main
import requests


# Simple test for HTTP method
class TestRequest(TestCase):

    BASE_URL = 'https://www.boredapi.com/api/activity'

    def test_request(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    main()