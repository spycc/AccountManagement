from Maccount import Maccount

class UserControl(Maccount):
    '''
    用户操作系统，负责功能操作
    总调度终端：usercontrol(self)
    添加控制：__addcontrol(self)
    修改控制：__revisecontrol(self)
    展示控制：__showcontrol(self)
    删除控制：__delcontrol(self)
    退出控制：__signout(self)
    '''


    def __addcontrol(self):
        '''
        添加流程
        '''
        a = 1
        while a == 1:
            print('请输入添加的帐号')
            name = input()
            print('请输入添加的密码')
            password = input()
            print('保存成功，帐号：' + name, '密码：' + password)
            print('按1继续添加，按2返回')
            a = int(input())
        else:
            self.usercontrol()

    
    def __revisecontrol(self):
        '''
        修改流程
        '''
        a = 1
        while a == 1:
            print('请输入要修改的帐号')
            name = input()
            print('请输入新密码')
            password = input()
            print ('保存成功，您的新密码' + password)
            print('按1继续修改，按2返回')
            a = int(input())
        else:
            self.usercontrol()


    def __showcontrol(self):
        '''
        展示流程
        '''
        Maccount.go(self,1)
        print('按2返回')
        input()
        self.usercontrol()


    def __delcontrol(self):
        '''
        删除流程
        '''
        a = 1
        while a == 1:
            print('请输入要删除的帐号')
            name = input()
            print('确认删除:y,重新输入：n')
            b = input()
            if b == 'n':
                continue
            print('帐号(name)已被成功删除')
            print('按1继续删除，按2返回')
            a = int(input())
        else:
            self.usercontrol()

    
    def __signout(self):
        '''
        退出流程
        '''
        print('感谢您的使用，再见！')


    def __inputerror(self):
        '''
        输入错误
        '''
        print('您输入有误，请重新输入')
        self.usercontrol()


    def usercontrol(self,usercommand = 1):
        '''
        总调度终端
        '''
        control = {1: self.__showcontrol, 2: self.__addcontrol,
                   3: self.__revisecontrol, 4: self.__delcontrol, 5: self.__signout}
        print('欢迎来到帐号管理系统：\n查询帐号(1)\n添加帐号(2)\n修改帐号(3)\n删除帐号(4)\n退出(5)')
        usercontrol = int(input())
        control.get(usercontrol, self.__inputerror)()
