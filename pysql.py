import pymysql


# 用来操作数据库的类
class MySQLCommand(object):
    # 类的初始化
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306  # 端口号
        self.user = 'root'  # 用户名
        self.password = "8495162"  # 密码
        self.db = "home"  # 库

    # 链接数据库
    def connectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        passwd=self.password, db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')

    # 插入数据
    def insertData(self, name, type, actor, score, date):
        try:
            #  cols = ', '.join(new_data.keys())
            #  rows = '"," '.join(new_data.values())
            #  sql = "INSERT INTO table01 (%s) VALUES (%s)" % (cols, '"' + rows + '"')
            sql0 = "SELECT * FROM table01 WHERE actor = '%s'" % actor
            result = self.cursor.execute(sql0)
            if result:
                print("数据已存在")
                return 0
            sql = "INSERT INTO table01 (name,type,actor,score,date)" "VALUES (%s,%s,%s,%s,%s)"
            values = (name, type, actor, score, date)
            try:
                self.cursor.execute(sql, values)
                self.conn.commit()
                print("插入成功")
            except pymysql.Error as e:
                self.conn.rollback()
                print("数据已回滚")
                print("插入数据失败，原因 %d: %s" % (e.args[0], e.args[1]))
        except pymysql.Error as e:
            print("数据库错误，原因%d: %s" % (e.args[0], e.args[1]))

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()  # 创建数据库操作类的实例
