import requests

token = 'xxxxxxxxxxxxxxxxx'
url = 'https://notify-api.line.me/api/notify'
headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}
session = requests.Session()
data = {'message': 'Hello'}
session.post(url, headers=headers, data=data)
