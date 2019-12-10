# 导包
import requests
# 获取session对象
session = requests.Session()

data = {"username": "13012345678", "password":"123456","verify_code":"8888"}
url_code = "http://localhost/index.php?m=Home&c=User&a=verify"
url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
url_order = "http://localhost/Home/Order/order_list.html"
# 请求验证码--->目的：自动记录服务器响应的cookies信息
session.get(url_code)
# 请求登录
session.post(url=url_login,data=data)
# 查看订单
response = session.get(url=url_order)
print("文本数据为：",response.text)
