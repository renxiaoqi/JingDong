import unittest

from HM import api
from HM.api.api_login import ApiLogin
from HM.tools.assert_common import assert_common


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        cls.apilogin = ApiLogin()
    # 登录
    def test01(self,mobile="13800000002",password="123456"):
        # 调用登录的方法
        r = self.apilogin.login(mobile,password)
        # 设置token
        token = r.json().get("data")
        print("获取到的token为：",token)
        # 将获取到的token添加到请求头中
        api.header["Authorization"] = "Bearer "+token
        # 断言
        print("登录成功之后的数据为：",r.json())
        assert_common(self,r)