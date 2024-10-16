import requests

request_url = requests.request(url="https://official-joke-api.appspot.com/random_joke", method="GET")
response = request_url.json()
question = response['setup']
answer = response['punchline']
print(f"Q: {question}")
print(f"A: {answer}")