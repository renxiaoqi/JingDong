import pymysql


class Util:
    __conn = None
    __cursor = None
    # 创建连接

    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host="127.0.0.1",
                                       user="root",
                                       password="root",
                                       port=3306,
                                       database="books",
                                       charset="utf8")
        return cls.__conn
    # 获取游标
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = Util.__get_conn().cursor()
        return   cls.__cursor
    # 执行sql语句
    @classmethod
    def run_sql(cls,sql):
        Util.__get_cursor()
        try:
            if sql.split()[0] == "select":
                cls.__cursor.execute(sql)
                return cls.__cursor.fetchall()
            else:
                raw = cls.__cursor.execute(sql)
                cls.__conn.commit()
                return raw
        except:
            cls.__conn.rollback()
            raise
        finally:
            Util.__close_cursor()
            Util.__close_conn()



    # 关闭游标
    @classmethod
    def __close_cursor(cls):
        if cls.__cursor is not None:
            cls.__cursor.close()
            cls.__cursor = None

    # 关闭连接
    @classmethod
    def __close_conn(cls):
        if cls.__conn is not None:
            cls.__conn.close()
            cls.__conn = None


