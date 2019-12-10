# 创建测试类
import json
import unittest

from parameterized import parameterized

from day03new import api
from day03new.api.api_login import ApiLogin
from day03new.tools.assert_common import assert_common


def data():
    aa = []
    with open("./data/testlogin.json","r") as f:
        for i in json.load(f).values():
            aa.append(tuple(i.values()))
            return aa


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.apilogin = ApiLogin()
    # 测试方法
    @parameterized.expand(data())
    def test01_login(self,mobile,password):
        # 调用登录方法
        response = self.apilogin.login(mobile,password)
        print("登录成功的响应数据为：",response.json())
        # 获取响应数据中的data并添加token
        token = response.json().get("data")
        print("登录成功后获取到的token为：",token)
        # 将token添加到headers中
        api.HEADERS["Authorization"] = "Bearer " + token
        print("登录之后的headers为：",api.HEADERS)
        # 断言
        assert_common(self,response)


