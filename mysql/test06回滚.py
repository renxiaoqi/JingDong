# 导包
import pymysql
# 创建链接
conn = pymysql.Connect(host="localhost",
                       user="root",
                       password="root",
                       port=3306,
                       database="books",
                       charset="utf8")
# 获取游标
cursor = conn.cursor()

# 执行sql语句
try:
    sql = "insert into t_hero1(name,gender,description,is_delete,book_id) values('王哈哈',0,'哈哈哈',0,1);"
    cursor.execute(sql)
    print("受影响的行数为：",cursor.rowcount)

    sql2 = "update t_hero1 set book_id=book_id+1 where id=2"
    cursor.execute(sql2)
    print("受影响的行数为：",cursor.rowcount)
    conn.commit()
except:
    conn.rollback()
    print("执行失败")
# 关闭游标
cursor.close()
# 关闭链接
conn.close()

# class TestAll():
#     conn = LianJie
