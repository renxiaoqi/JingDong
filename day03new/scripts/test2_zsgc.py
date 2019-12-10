import unittest

from day03new import api
from day03new.api.api_case import ApiCase
from day03new.tools.assert_common import assert_common


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.apicase = ApiCase()
    # 添加员工
    def test1_add(self,username="dhfkjhji",mobile="15046538795",worknumber="59873"):
        response = self.apicase.insert_user(username,mobile,worknumber)
        print("添加之后的响应数据为：",response.json())
        # 获取添加员工之后的id
        api.USER_ID = response.json().get("data").get("id")
        print("获取到的id为：",api.USER_ID)
        assert_common(self,response)
    # 修改员工信息
    def test2_update(self,username="k55k6kkk"):
        response = self.apicase.update_user(username)
        print("修改之后的响应数据为：",response.json())
        # 断言
        assert_common(self,response)
    # 查询员工信息
    def test3_selete(self):
        response = self.apicase.select_user()
        print("查询到的响应数据为：",response.json())
        # 断言
        assert_common(self, response)
    # 删除员工
    def test4_delete(self):
        response = self.apicase.delete_user()
        print("删除之后的响应数据为：",response)
        # 断言
        assert_common(self,response)

