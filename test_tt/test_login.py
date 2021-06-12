import json

import requests

url = "https://eauth.downtown8.net/passport/login"
# header = {"Content-Type": "application/json"}
header = {"Content-Type": "application/x-www-form-urlencoded"}
# params = {"passport": "758737541@qq.com", "pwd": "DZh123456", "passportType": "email", "countryCode": "1"}
data = {"passport": "758737541@qq.com", "pwd": "DZh123456", "passportType": "email", "countryCode": "1"}
result = requests.post(url=url, data=data, headers=header)
print(data)
print(url)
# print(header)
print(str(result) + "========")
print(result.text)
