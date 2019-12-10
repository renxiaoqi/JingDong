import time
import unittest

# 创建测试类
from test_tpshop.tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts",pattern="test*.py")

# 运行测试套件
with open("./report/login{}.html".format(time.strftime("%Y_%m_%d_%M_%H_%S")),"wb") as f:
    HTMLTestRunner(stream=f).run(suite)