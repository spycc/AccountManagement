from Maccount import Maccount

class Func(Maccount):
    '''
    系统各功能
    查询全部、查询单个、添加功能、修改功能、删除功能
    '''
    
    @classmethod
    def funcqueryall(cls):
        '''
        查询全部功能
        '''
        data = Maccount.queryaccount()
        if data != '':
            for id, user, passwd in data:
                print('id:' + str(id) + '     user:' + user + '     passwd:' + passwd)
            print('已查询完成')
        else:
            print('该数据表为空')

    
    @classmethod
    def funcqueryone(cls, seach):
        '''
        信息搜索功能，接受一个参数进行信息匹配，再把匹配到的数据返回
        '''
        data = Maccount.queryaccount(seach)
        if data == ():
            print('查询无结果')
        else:
            for id, user, passwd in data:
                print('id:' + str(id) + '     user:' + user + '     passwd:' + passwd)
            print('已查询完成')


    @classmethod
    def funcadd(cls):
        '''
        添加功能
        '''
        print('请输入添加的帐号')
        name = input()
        print('请输入添加的密码')
        password = input()
        Maccount.addaccount(name, password)
        print('保存成功')

    
    @classmethod
    def funcrevise(cls):
        '''
        修改功能
        '''
        print('请输入要修改的帐号')
        name = input()
        data = Maccount.queryaccount(name)
        if data == ():
            print('您要修改的信息不存在，请重新输入')
            cls.funcrevise()
        else:
            print('请输入新密码')
            password = input()
            Maccount.reviseaccount(name,password)
            print ('密码成功修改为:' + password)


    @classmethod
    def funcdel(cls):
        '''
        删除功能
        '''
        print('请输入要删除的帐号')
        name = input()
        print('确认删除:y,重新输入请按任意键')
        b = input()
        if b == 'y':
            data = Maccount.queryaccount(name)
            if data == ():
                print('您要删除的信息不存在，请重新输入')
                cls.funcdel()
            else:
                Maccount.delaccount(name)
                print('帐号('+name+')已被成功删除')
        else:
            Func.funcdel()
