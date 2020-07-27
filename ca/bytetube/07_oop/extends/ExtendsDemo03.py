class Master(object):
    def __init__(self):
        print("master init")
        self.kongfu = '[Master method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')


# 创建学校类
class School(object):
    def __init__(self):
        print("School init")
        self.kongfu = '[bytetube method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')

    def make_cake2(self):
        print(f'{self.kongfu} to make cake')


class Prentice(Master,School):
    pass


prentice = Prentice()#Prentice基于Master,如果想创建子类对象，一定是先创建父类对象，再创建子类对象
print(prentice.kongfu)#[bytetube method]
prentice.make_cake()#[bytetube method] to make cake
prentice.make_cake2()