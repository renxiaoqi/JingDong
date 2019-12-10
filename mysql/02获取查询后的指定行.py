# 导包
import pymysql

# 创建连接
conn = pymysql.Connect(host="localhost",
                       user="root",
                       password="root",
                       port=3306,
                       database="books",
                       charset="utf8")
# 获取游标对象
cursor = conn.cursor()
# 执行sql
sql = "select * from t_book"
cursor.execute(sql)
# 拿取数据
# one = cursor.fetchone()
# print(one)
# all = cursor.fetchall()
# print(all)
any = cursor.fetchmany(4)
print(any)
# 返回受影响的行
now = cursor.rowcount

print("受影响的行数为：",now)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()