import requests
from decouple import config
import json

API_KEY = config("API_KEY")
API_URL_ENDPOINT = config("API_URL_ENDPOINT")
API_PER_REQUEST_LIMIT_COUNT = 50

HEADERS = {
    "Authorization": API_KEY
}


def fetch_data(cuisine, total_records=1000):
    with open(cuisine+'.json', 'w') as writer:
        records = []
        for count in range(0, total_records, API_PER_REQUEST_LIMIT_COUNT):
            params = {
                "location": "New York City",
                "term": cuisine,
                "categories": "Restaurants",
                "limit": API_PER_REQUEST_LIMIT_COUNT,
                "offset": count
            }
            response = requests.get(API_URL_ENDPOINT, params=params, headers=HEADERS).json()
            for record in response['businesses']:
                records.append(record)
            print ("%d %s cuisine records fetched" % (count+API_PER_REQUEST_LIMIT_COUNT, cuisine))
        json.dump(records, writer)


if __name__ == "__main__":
    CUISINES_LIST = ['Indian', 'Mexican', 'Chinese', 'Korean', 'Japanese']
    for cuisine in CUISINES_LIST:
        fetch_data(cuisine)