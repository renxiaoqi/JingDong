class ApiLogin:
    # 初始化
    def __init__(self,session):
        self.url_code = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
        self.session = session
    # 获取验证码
    def api_verify_code(self):
        self.session.get(url=self.url_code)

    # 登录
    def api_login(self,username,password,verify_code):
        data = {"username":username,"password":password,"verify_code":verify_code}
        return self.session.post(url=self.url_login,data=data)
