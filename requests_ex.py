import requests

session=requests.Session()
response=requests.get("https://google.co.in", cookies={"new-cookie-identifier": "1234abcd"})

print (response.request.headers)
print (response.status_code)