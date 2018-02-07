
class Proving():
    '''
    输入验证机制，包括流程验证和信息验证
    '''

    @classmethod
    def prtwochoose(cls):
        '''
        2选项输入验证,判断输入是否是1-2.
        '''
        a = input()
        while a not in ['1', '2']:
            print('您输入的指令有误，请重新输入')
            a = input()
        else:
            return a
