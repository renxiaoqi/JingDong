# 导包
import requests
# 获取响应信息头
response = requests.get("http://www.baidu.com")
# 获取响应编码格式
print("响应信息头为：",response.headers)
# 设置编码格式
print("默认响应编码是：",response.encoding)
# 设置编码格式
# response.encoding = "utf-8"
response.encoding = "gbk"

print(response.text)