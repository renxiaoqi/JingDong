# 创建测试套件
import unittest

import time


from day03new.tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts")

# 运行测试套件
# with open("./report/login{}.html".format(time.strftime("%H_%M_%S")),"wb") as f:
#     HTMLTestRunner(f).run(suite)
unittest.TextTestRunner().run(suite)