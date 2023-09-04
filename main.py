import requests


# I create a BoredAPIWrapper class with a constructor __init__
class BoredAPIWrapper:
    BASE_URL = 'https://www.boredapi.com/api/activity'

    def __init__(self):
        pass

    def get_random_activity(self, activity_type=None, participants=None, price=None, accessibility=None):
        params = {}

        if activity_type:
            params['type'] = activity_type

        if participants:
            params['participants'] = participants

        if price:
            params['price'] = price

        if accessibility:
            params['accessibility'] = accessibility

        # Inside the get_random_activity method, I construct the URL with the specified parameters
        # and make a GET request to the Bored API.
        response = requests.get(self.BASE_URL, params=params)

        # If the request is successful (status code 200), we return the JSON response.
        # Otherwise, we raise an exception with an error message.
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch activity. Status code: {response.status_code}")


# Example usage:
bored_api = BoredAPIWrapper()
activity = bored_api.get_random_activity(activity_type="relaxation", participants=1, price=0, accessibility=0.5)
print(activity)
