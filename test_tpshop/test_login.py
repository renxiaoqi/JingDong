import json
import unittest
import requests
from parameterized import parameterized
from test_tpshop.api.api_login import ApiLogin


def get_data(filename):

    with open("./data/"+filename,"r",encoding="utf-8") as f:
        arr = []
        for data in json.load(f).values():
            arr.append(tuple(data.values()))
        return arr
        # print(arr)


# get_data("login.json")
# 创建测试类
class LoginCase(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取session对象
        cls.session = requests.session()
        # 获取
        cls.login = ApiLogin(cls.session)
    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    # 测试方法
    @parameterized.expand(get_data("login.json"))
    def test01(self,username,password,verify_code,excape):
        self.login.api_verify_code()
        aa = self.login.api_login(username,password,verify_code)
        self.assertEqual(excape,aa.json().get("status"))