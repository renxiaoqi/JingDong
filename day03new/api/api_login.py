import requests

from day03new.api import BASE_URL, HEADERS


class ApiLogin(object):
    def __init__(self):
        self.login_url = BASE_URL + "/api/sys/login"
    # 登录
    def login(self,mobile,password):
        data = {"mobile":mobile,"password":password}
        return requests.post(url=self.login_url, json=data, headers=HEADERS)

