import requests

IP = str(input("IP: "))

request_url = requests.request(url=f"https://ipinfo.io/{IP}/geo", method="GET")
response = request_url.json()
print(response)