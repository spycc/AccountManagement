from Func import Func

class Flow():
    '''
    系统流程控制器
    1.查询分支
    2.添加分支
    3.修改分支
    4.删除分支
    5.退出分支
    '''
    
    @classmethod
    def flowmain(cls):
        flowlist = {1: cls.__flowquery, 2: cls.__flowadd,
                    3: cls.__flowrevise, 4: cls.__flowdel, 5: cls.__flowout}
        print('欢迎来到帐号管理系统：\n查询帐号(1)\n添加帐号(2)\n修改帐号(3)\n删除帐号(4)\n退出(5)')
        user = int(input())
        flowlist.get(user, cls.__errmaininput)()
    

    @classmethod
    def __flowquery(cls):
        '''
        查询流程分支
        '''
        Func.funcqueryall()
        print('按2返回')
        input()
        cls.flowmain()


    @classmethod
    def __flowadd(cls):
        '''
        添加流程分支
        '''
        a = 1
        while a == 1:
            Func.funcadd()
            print('按1继续添加，按2返回')
            a = int(input())
        else:
            cls.flowmain()
        

    @classmethod
    def __flowrevise(cls):
        '''
        修改流程分支
        '''
        a = 1
        while a == 1:
            Func.funcrevise()
            print('按1继续修改，按2返回')
            a = int(input())
        else:
            cls.flowmain()
    

    @classmethod
    def __flowdel(cls):
        '''
        删除流程分支
        '''
        a = 1
        while a == 1:
            Func.funcdel()
            print('按1继续删除，按2返回')
            a = int(input())
        else:
            cls.flowmain()
    

    @classmethod
    def __flowout(cls):
        '''
        退出流程分支
        '''
        print('感谢您的使用，再见！')



    @classmethod
    def __errmaininput(cls):
        print('您输入的指令有误，请重新输入')
        cls.flowmain()
