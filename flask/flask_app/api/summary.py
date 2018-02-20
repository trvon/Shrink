import json, requests

def send_request(url):
    # This is based off the documentation at
    # https://smmry.com/api
    destination = 'https://api.smmry.com'
    payload = {'SM_API_KEY': 'C19B21C4CD','SM_URL':url}
    return requests.post(destination, params=payload).text[0:]
