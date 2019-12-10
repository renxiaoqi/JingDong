# 导包
import requests
# 调用post方法
url = "http://182.92.81.159/api/sys/login"
data = {"mobile":13012345678,"password":123456}
response = requests.post(url,json=data)
# 查看响应状态码
print("响应状态码为：",response.status_code)
# 查看响应头的信息
print("响应头的信息为：",response.headers)
# print("head信息为：",requests.head(url))
# print("项目支持的方法为：",requests.options(url))
