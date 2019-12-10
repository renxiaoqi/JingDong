


class SQL():
    __conn = None
    __cursor = None
    # 创建连接
    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host="localhost",
                                       user="root",
                                       password="root",
                                       port=3306,
                                       database="books",
                                       charset="utf8")
        return cls.__conn
    # 获取游标对象
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = SQL.__get_conn().cursor()
        return cls.__cursor
    # 执行sql
    @classmethod
    def execate_sql(cls,sql):
        SQL.__get_cursor()
        try:
            if sql.split()[0] == "select":
                cls.__cursor.execute(sql)
                return cls.__cursor.fetchall()
            else:
                row = cls.__cursor.execute(sql)
                cls.__conn().commit()
                return row
        except:
            cls.__conn().rollback()
            raise
        finally:
            SQL.__close_cursor()
            SQL.__close_conn()





    # 关闭游标
    @classmethod
    def __close_cursor(cls):
        if SQL.__cursor is not None:
            cls.__cursor.close()
            cls.__cursor = None

    # 关闭连接
    @classmethod
    def __close_conn(cls):
        if SQL.__conn is not None:
            cls.__conn.close()
            cls.__conn = None


