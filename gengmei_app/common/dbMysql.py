# -*- coding: UTF-8 -*-

import pymysql

class Mysql(object):
    def __init__(self, host, port, user, password, db, charset='utf8', cursorclass=pymysql.cursors.DictCursor):
        """初始化mysql连接"""
        try:
            self.conn = pymysql.connect(host, user, password, db, int(port), charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        except pymysql.Error as e:
            errormsg = 'Cannot connect to server\nERROR(%s):%s' % (e.args[0],e.args[1])
            print(errormsg)
            exit(2)
        self.cursor = self.conn.cursor()

    def exec(self,sql):
        """执行dml,ddl语句"""
        try:
           self.cursor.execute(sql)
           self.conn.commit()
        except:
           self.conn.rollback()

    def query(self,sql):
        """查询数据"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def __del__(self):
        """ 关闭mysql连接 """
        self.conn.close()
        self.cursor.close()

if __name__ == '__main__':
    # mysql_test = Mysql('152.136.57.57', '3306', 'root', '5OqYM^zLwotJ3oSo', 'maidian')
    mysql_test = Mysql('bj-cdb-6slgqwlc.sql.tencentcdb.com', '62120', 'work', 'Gengmei1', 'maidian_data')
    # 创建表
    # mysql_test.exec('create table t1 (id int auto_increment primary key,timestamp TIMESTAMP)')
    # 插入数据
    # mysql_test.exec('insert into t1 (id,timestamp) value (NULL,CURRENT_TIMESTAMP)')
    # 查询数据
    result = mysql_test.query('select * from maidian_history_data where device_id ="868080041007173" order by create_time desc')
    print(result[0]['create_time'])
    # 删除数据
    # mysql_test.exec('delete from t1 where id = 1')
