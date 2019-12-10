# 导包
import pymysql
# 创建链接
conn = pymysql.Connect(host="127.0.0.1",
                       user="root",
                       password="root",
                       port=3306,
                       database="books",
                       autocommit=True,
                       charset="utf8"
                       )
# 获取游标对
cursor = conn.cursor()
# 执行sql语句bhgghybcnjf-]=[poiuy````````````````````````````````````````
# sql = "insert into t_hero1 values(0,'王哈哈',0,'哈哈哈',0,1);"
sql = "insert into t_hero1(name,gender,description,is_delete,book_id) values('王哈哈',0,'哈哈哈',0,1);"
cursor.execute(sql)
# 获取受影响的行数
print("受影响的行数为：",cursor.rowcount)
print(cursor.fetchmany(2))
# 关闭游标
cursor.close()
# 关闭链接
conn.close()