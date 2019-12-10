import unittest

from HM import api
from HM.api.api_employee import ApiEmployee
from HM.tools.assert_common import assert_common


class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取ApiEmployee对象
        cls.apiemployee = ApiEmployee()
    # 新增员工
    def test01_add(self,username="shengou8546233",mobile="13045987651",workNumber="5894613"):
        # 调用新增员工方法
        response = self.apiemployee.add_user(username,mobile,workNumber)
        # 提取id
        api.USER_ID = response.json().get("data").get("id")
        print("新增员工的id为：",api.USER_ID)
        # 断言
        assert_common(self,response)
    # 更新员工信息
    def test02_update(self,username="wowowwjkk"):
        response = self.apiemployee.update_user(username)
        print("更改信息之后的响应数据为：",response.json())
        assert_common(self,response)
    # 查询员工信息
    def test03_select(self):
        response = self.apiemployee.select_user()
        print("查询id为{}的学生信息为：".format(api.USER_ID),response.json())
    # 删除员工信息
    def test05_delete(self):
        # 调用删除业务方法
        r = self.apiemployee.delete_user(api.USER_ID)
        print("删除数据后的结果为：",r.json())

        # 断言
        assert_common(self,r)

