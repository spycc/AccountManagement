class Proving():
    '''
    输入验证机制，包括流程验证和信息验证
    '''

    def prmainflow(self,user):
        '''
        主流程输入错误提示
        传入一个验证参数，判断是否属于主流程的6个数字之中，如果是，则执行，不是则提示重新输入
        '''
        if user in [1,2,3,4,5]:
            return True
        else:
            return False
