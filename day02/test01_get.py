"""
目标

"""
# 导包
import requests
# 调用get方法
response = requests.get("http://www.baidu.com")
# 查看响应状态码
print(response.status_code)
print("-"*10)
# 查看响应数据文本
print(response.text)