# 导包
import pymysql

# 创建连接
pymysql.connect()
conn = pymysql.Connect(host="localhost",
                       user="root",
                       password="root",
                       port=3306,
                       database="books",
                       autocommit=False,
                       charset="utf8")

# 获取游标对象
cursor = conn.cursor()
# 执行sql语句
sql = "select * from t_book"
num = cursor.execute(sql)
print("受影响的行数为：",num)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()