# 导包
import requests
# 调用get方法
# response = requests.get("https://www.baidu.com")
# # 查看响应状态码
# print("响应状态码为：",response.status_code)
# # 查看响应文本数据
# print("响应文本数据为：",response.text)
# # 查看编码
# print("编码为：",response.encoding)
# # 更改编码格式
# response.encoding = "utf-8"
# print("响应文本数据为：",response.text)
# # 获取cookie
# print("cookies信息为：",response.cookies)
# print("cookies的值为：",response.cookies["BDORZ"])

# 传递url参数
url = "http://www.baidu.com/s"
response = requests.get(url,params="wd=python")
print("响应状态码为：",response.status_code)
response.encoding = "utf-8"
print("响应url为：",response.url)
print("响应文本数据为：",response.text)