"""
需求：
    1.请求url = "http://www.baidu.com/?name=张三"
    2.请求url = "http://www.baidu.com/?name=张三"
    查看url：响应对象.url
"""
# 导包
import requests
# 调用get方法
# 方法一
# response = requests.get("http://www.baidu.com")
# 方法二
url = "http://www.baidu.com"
response = requests.get(url,params="name=张三")
# 方法三
# url = "http://www.baidu.com"
# data = {"name":"张三","age":18}
# response = requests.get(url,params=data)
# 查看响应状态码
print(response.status_code)
print("-"*10)
# 查看请求url
print(response.url)