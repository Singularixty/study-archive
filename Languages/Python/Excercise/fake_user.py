import requests


request_ = requests.request(url="https://randomuser.me/api/", method="GET")
response = request_.json()

