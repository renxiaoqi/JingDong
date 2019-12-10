def assert_common(ss,resp,status_code=200, code=10000, message="操作成功"):
    # 断言响应状态码
    ss.assertEqual(status_code,resp.status_code)
    #断言success
    ss.assertTrue(resp.json().get("success"))
    # 断言code
    ss.assertEqual(code,resp.json().get("code"))
    # 断言message
    ss.assertIn(message,resp.json().get("message"))


