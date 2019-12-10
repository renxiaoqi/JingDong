import pymysql


# 获取链接对象
conn = pymysql.Connect(host="localhost",
                       user="root",
                       password="root",
                       port=3306,
                       database="books",
                       charset="utf8",
                       autocommit=False, )
# 获取游标对象
cursor = conn.cursor()
# 执行sql语句
# 添加
sql = "insert into t_hero1 values(0,'张三三',5,'hehehe',1,0)"
# 删除
# sql = "delete from t_hero1 where id=9"
# 修改
# sql = "update t_hero1 set name='三三',description='无' where id=8"
# 清空表中所有数据，并保留表结构
# sql = "truncate table t_hero1"
print("受影响的行数为：",cursor.execute(sql))
# 查询
sql2 = "select * from t_hero1"
print("受影响的行数为：",cursor.execute(sql2))
print(cursor.fetchall())
# 关闭游标
cursor.close()
# 关闭链接
conn.close()