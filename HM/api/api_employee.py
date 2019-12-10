import requests

from HM import api


class ApiEmployee():
    #初始化
    def __init__(self):
        # 新增员工url
        self.add_url = api.BASE_URL + "/api/sys/user"
        # 修改删除查询url
        self.user_url = api.BASE_URL + "/api/sys/user/{}"
    # 添加员工
    def add_user(self,username,mobile,workNumber):
        # 定义data
        data = {"username": username,
                "mobile": mobile,
                "workNumber": workNumber}
        # 调用post方法
        return requests.post(url=self.add_url,json=data,headers=api.header)
    # 修改员工
    def update_user(self,username):
        data = {"username":username}
        return requests.put(url=self.user_url.format(api.USER_ID),json=data,headers=api.header)
    # 查询员工
    def select_user(self):
        return requests.get(url=self.user_url.format(api.USER_ID),headers=api.header)
    # 删除员工
    def delete_user(self,user_id):
        return requests.delete(url=self.user_url.format(user_id),headers=api.header)

