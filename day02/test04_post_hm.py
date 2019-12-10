# 导包
import json

import requests
import json
# 调用post方法
url = "http://182.92.81.159/api/sys/login"
data = '{"mobile":"13800000002", "password":"123456"}'
# response = requests.post(url,json=data)
response = requests.post(url,data=json.loads(data))
# 查看响应状态码
print(response.status_code)
# 查看响应数据
print(response.text)
