from mysql.zsgc import Util

sql = "insert into t_book (`title`,`pub_date`,`read`,`comment`,`is_delete`)VALUES('东游记','1990-08-12',20,30,0)"
# sql = "select * from t_hero1"
print(Util.run_sql(sql))