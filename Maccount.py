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
    def queryaccount(cls, user=''):
        '''
        信息查询，接受一个用户名参数，返回帐号相关的所有信息。
        1.如参数为空，则返回所有数据库数据
        2.如参数有内容，则查询对应帐号，并返回帐号的信息如无该帐号，则返回False
        '''
        conn, cur = cls.__openmysql()
        if user == '':
            cur.execute('SELECT * FROM accounts')
            return cur.fetchall()
        else:
            return ('未完成')
        cls.__closemysql(conn, cur)

    @classmethod
    def add(cls, user='', passwd=''):
        '''
        添加数据到数据库
        1,只传入不为空的数据
        '''
        conn, cur = cls.__openmysql()
        if user != '' and passwd != '':
            print (user+passwd)
            # cur.execute("insert into `accounts`(`username`,`password`)values(%s,%s)"%(user,passwd))
            # conn.commit()
        elif user == '' and passwd != '':
            pass
        else:
            pass
        cls.__closemysql(conn, cur)


        
