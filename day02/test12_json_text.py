# 导包
import requests
# 查看响应cookies
response = requests.get("http://192.168.38.63:8000/api/departments/")
# 以text形式解析数据
print("文本形式为：",type(response.text),response.text)
# 以json形式解析数据
print("json数据为：",type(response.json()),response.json())
print(response.json().get("dep_name"))