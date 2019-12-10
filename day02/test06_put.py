"""
    目标：以标准的RESTful风格项目，演示下json与data
    需求：
        学院资源更新
"""
# 导包
import requests
import json
# 调用post方法
url = "http://192.168.38.63:8000/api/departments/T01887/"
data = {
			"data": [
					  {
						"dep_id": "T01887",
						"dep_name": "Test学院1887",
						"master_name": "Test-Master03",
						"slogan": "Here is Slogan03"
					  }
					]
		}
r = requests.put(url=url, json=data)
# 获取响应状态码
print(r.status_code)
# 以json形式获取响应结果
print(r.json())