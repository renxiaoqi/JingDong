import requests
url = "http://localhost/index.php?m=Home&c=User&a=verify"
response = requests.get(url)
cookie = response.cookies
print("cookies为：",cookie)
print("cookies的值为：",cookie["PHPSESSID"])