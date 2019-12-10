import requests
from HM import api


class ApiLogin:
    # 初始化
    def __init__(self):
        self.url = api.BASE_URL+"/api/sys/login"
    #登录
    def login(self,mobile,password):
        data = {"mobile":mobile,"password":password}
        return requests.post(url=self.url,json=data,headers=api.header)



