import pymysql.cursors

class Maccount():
    '''
    数据传输程序，用于对数据库内容的查询、读取和存入
    打开数据库：__openmysql(self)
    关闭数据库：__closemysql(self)
    帐号信息查询：__queryaccount(self)
    '''

    @classmethod
    def __openmysql(cls):
        '''
        打开数据库,返回两个参数conn和cur
        '''
        conn = pymysql.connect(host='localhost', user='root', passwd='111111', db='sldata', charset='utf8mb4')
        cur = conn.cursor()
        return conn,cur
    

    @classmethod
    def __closemysql(cls, conn, cur):
        '''
        关闭数据库，接受两个参数conn和cur
        '''
        cur.close()
        conn.close()
    

    @classmethod
    def queryaccount(cls, seach=''):
        '''
        信息查询，支持全部和单条消息查询。
        1.查询全部：参数为空是查询该表全部数据
        2.查询单条：如参数有内容，则查询对应username，返回帐号的信息如无该帐号，则返回（）
        '''
        conn, cur = cls.__openmysql()
        if seach == '':
            cur.execute('SELECT * FROM accounts')
            data = cur.fetchall()
        else:
            sqlcount = "SELECT * FROM accounts WHERE username ='{}'".format(seach)
            cur.execute(sqlcount)
            data = cur.fetchall()
        cls.__closemysql(conn, cur)
        return data



    @classmethod
    def addaccount(cls, user, passwd):
        '''
        添加数据到数据库
        1，添加帐号和密码：传入2个参数
        2，修改密码：传入密码参数
        3，修改帐号：传入帐号参数
        '''
        conn, cur = cls.__openmysql()
        sqlcount = "insert into accounts(username, password)values('{}','{}')".format(user,passwd)
        cur.execute(sqlcount)
        conn.commit()
        cls.__closemysql(conn, cur)



    @classmethod
    def reviseaccount(cls,user,passwd):
        conn,cur = cls.__openmysql()
        sqlcount = "update accounts set password = '{}' where username = '{}'".format(passwd,user)
        cur.execute(sqlcount)
        conn.commit()
        cls.__closemysql(conn,cur)



    @classmethod
    def delaccount(cls, name):
        '''
        数据删除程序
        '''
        conn,cur = cls.__openmysql()
        sqlcount = "delete from accounts where username = '{}'".format(name)
        cur.execute(sqlcount)
        conn.commit()
        cls.__closemysql(conn, cur)




        
