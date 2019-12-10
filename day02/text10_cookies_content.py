# 导包
import requests
# 查看响应cookies
response = requests.get("https://www.baidu.com")
print("响应cookies为：",response.cookies)
# 获取cookie的值
print(response.cookies["BDORZ"])
