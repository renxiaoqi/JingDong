# 导包
import requests
# 调用delete方法
url = "http://192.168.38.63:8000/api/departments/T01887/"
response = requests.delete(url)
# 查看响应状态码：204
print(response.status_code)
# 查看响应数据：为空
print(response.text)