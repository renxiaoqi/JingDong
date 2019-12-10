# 导包
import pymysql
# 创建链接
conn = pymysql.Connect(host="localhost",
                       user="root",
                       password="root",
                       port=3306,
                       database="books",
                       autocommit=True,
                       charset="utf8")
# 获取游标
cursor = conn.cursor()
# 执行sql语句
sql = "update t_hero1 set book_id=book_id+1 where id=2"
cursor.execute(sql)
print("受影响的行数为：",cursor.rowcount)
# 关闭游标
cursor.close()
# 关闭链接
conn.close()
