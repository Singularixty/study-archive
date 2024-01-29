import requests

payload = {'firstname' : 'hello', 'lastName' : 'singularixty', 'email' : 'singularixty@example.com'}
response_get = requests.get('https://httpbin.org/get', params=payload)
print(response_get.url)
print(response_get.text)
response_json = response_get.json()
print(response_json['args']['email'])

files = {'file': open('./bin/finance_data.csv', 'rb')}
response_post = requests.post('https://httpbin.org/post',files=files)
print(response_post.url)
print(response_post.text)