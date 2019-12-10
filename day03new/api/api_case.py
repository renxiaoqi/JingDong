import requests

from day03new import api
from day03new.api import BASE_URL, HEADERS


class ApiCase(object):
    def __init__(self):
        self.insert_url = BASE_URL + "/api/sys/user"
        self.other_url = BASE_URL + "/api/sys/user/{}"

    # 添   加
    def insert_user(self,username,mobile,worknumber):
        data = {"username": username,
                 "mobile": mobile,
                 "workNumber": worknumber}
        return requests.post(url=self.insert_url, json=data, headers=HEADERS)
    # 修改
    def update_user(self,username):
        data = {"username": username}
        return requests.put(url=self.other_url.format(api.USER_ID), json=data, headers=HEADERS)
    # 查看
    def select_user(self):
        return requests.get(url=self.other_url.format(api.USER_ID),headers=api.HEADERS)
    # 删除
    def delete_user(self):
        return requests.delete(url=self.other_url.format(api.USER_ID),headers=api.HEADERS)
