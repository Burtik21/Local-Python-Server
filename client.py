import requests
import json
url_based = "http://127.0.0.1:5000/"
endpoint = "/post-number"
url = url_based + endpoint

data = {
    "number": "35"
}
headers = {'Content-Type': 'application/json'}

res = requests.post(url,json=data, headers=headers)
print(res.text)