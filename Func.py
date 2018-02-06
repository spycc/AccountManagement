from Maccount import Maccount

class Func(Maccount):
    '''
    系统各功能
    查询全部、添加功能、修改功能、删除功能
    '''
    
    @classmethod
    def funcqueryall(cls):
        '''
        查询全部功能
        '''
        data = Maccount.queryaccount()
        for id, user, passwd in data:
            print('id:' + str(id) + '     user:' +
                  user + '     passwd:' + passwd)
        print('已展示完成')


    @classmethod
    def funcadd(cls):
        '''
        添加功能
        '''
        print('请输入添加的帐号')
        name = input()
        print('请输入添加的密码')
        password = input()
        Maccount.add(name,password)
        print('保存成功')

    
    @classmethod
    def funcrevise(cls):
        '''
        修改功能
        '''
        print('请输入要修改的帐号')
        name = input()
        print('请输入新密码')
        password = input()
        print ('保存成功，您的新密码' + password)


    @classmethod
    def funcdel(cls):
        '''
        删除功能
        '''
        print('请输入要删除的帐号')
        name = input()
        print('确认删除:y,重新输入：任意键')
        b = input()
        if b == 'y':
            print('帐号('+name+')已被成功删除')
        else:
            Func.funcdel()
