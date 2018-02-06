import pymysql.cursors

class Maccount():
    '''
    帐号管理类，主要功能如下：
    执行程序：go(self)
    打开数据库：__openmysql(self)
    关闭数据库：__closemysql(self)
    帐号添加：__addaccount(self)
    帐号删除：__delaccount(self,delid)
    帐号修改：__reviseaccount(self, revisepr, delid)
    帐号展示：__showaccount(self)
    帐号查询：__queryaccount(self)
    '''

    def __openmysql(self):
        '''
        打开数据库,返回两个参数conn和cur
        '''
        conn = pymysql.connect(host='localhost', user='root', passwd='111111', db='sldata', charset='utf8mb4')
        cur = conn.cursor()
        return conn,cur
    
    def __closemysql(self,conn,cur):
        '''
        关闭数据库，接受两个参数conn和cur
        '''
        cur.close()
        conn.close()


    def __addaccount(self,username,userpassword):
        '''
        往数据库添加新帐号
        '''
        conn,cur = self.__openmysql()



    def __delaccount(self,username):
        '''
        删除数据库对应帐号
        '''
        pass


    def __reviseaccount(self, revisepr, delid):
        '''
        修改数据库中对应帐号或密码
        '''
        pass


    def __showaccount(self):
        '''
        展示所有账户
        '''
        conn, cur = self.__openmysql()
        cur.execute('SELECT * FROM accounts')
        return cur.fetchall()
        self.__closemysql(conn, cur)
    

    def __queryaccount(self, user):
        '''
        帐号信息查询，接受一个帐号，返回帐号相关信息。
        '''
        pass

    

    
    def go(self,zl):
        '''
        执行函数
        '''
        funclist = {1:self.__showaccount, 2:self.__queryaccount, 3:self.__addaccount ,4:self.__reviseaccount, 5:self.__delaccount,}
        funclist[zl]()

        
