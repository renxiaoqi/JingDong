# 导包
import requests
# 查看响应cookies
response = requests.get("https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1575703331&di=1ab928a5524ef44cd68ee8018e5dcd84&src=http://p3.ssl.cdn.btime.com/t0112a92470e204868b.jpg?size=500x313")
content = response.content
print("字节码为：",content)
with open("./故宫.jpg","wb") as f:
    f.write(content)


