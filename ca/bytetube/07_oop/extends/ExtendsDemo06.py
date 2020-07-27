class Master(object):
    def __init__(self):
        self.kongfu = '[Master method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')


class School(object):
    def __init__(self):
        self.kongfu = '[bytetube method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[original method]'

    def make_cake(self):
        # 如果是先调用了父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己子类的初始化
        self.__init__()
        print(f'{self.kongfu} to make cake')

        # 调用父类方法，但是为保证调用到的也是父类的属性，必须在调用方法前调用父类的初始化

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 徒孙类
class Grand(Prentice):
    pass


grand = Grand()

grand.make_cake()  # '[original method]' to make cake

grand.make_school_cake()  # bytetube method  to make cake

grand.make_master_cake()  # mater method  to make cake