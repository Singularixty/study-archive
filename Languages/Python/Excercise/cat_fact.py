import requests

url_request = requests.request(url="https://catfact.ninja/fact", method="GET")
response = url_request.json()
fact = response['fact']
length = response['length']

print(fact)
print(length)