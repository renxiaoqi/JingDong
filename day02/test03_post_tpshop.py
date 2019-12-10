# 导包
import json

import requests

# 调用post方法
url = "http://localhost/index.php?m=Home&c=User&a=do_login"
data = {"username": 13088888888, "password": 123456, "verify_code": 8888}
response = requests.post(url,data=data)
# 查看响应状态码
print(response.status_code)
# 查看响应数据
print(response.text)
print("head信息为：",requests.head(url))