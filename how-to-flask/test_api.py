"""Use this to test the sample API.

We simply set up the payload and headers and attempt to ask our new webapp
for some gibberish.
"""
import requests

GIBBERISH_ENDPOINT = 'http://localhost:8888/gibberish'

payload = {
    'num_words': 10,
    'max_word_length': 12
}

# These tell the app that there is a json blob attached to the request with
# our data in it.
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# This makes the actual request to the endpoint using the POST protocol.
response = requests.post(
    GIBBERISH_ENDPOINT,
    json=payload,
    headers=headers
)

print response.json()
