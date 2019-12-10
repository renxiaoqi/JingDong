def assert_common(self,r,code=200,msg="操作成功"):
    # 判断响应状态码
    self.assertEqual(code,r.status_code)
    # 断言success
    self.assertTrue(r.json().get("success"))
    # 断言message
    self.assertIn(msg,r.json().get("message"))
    # 断言code
    self.assertEqual(10000,r.json().get("code"))










