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
        # 定义私有属性
        self.__money = 20

    # 定义私有方法
    def __info_print(self):
        print(self.kongfu)
        print(self.__money)

    def make_cake(self):
        self.__init__()
        print(f'{self.kongfu} to make cake')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 徒孙类
class Grand(Prentice):
    pass


prentice = Prentice()
# 对象不能访问私有属性和私有方法
# print(prentice.__money)
# prentice.__info_print()

grand = Grand()
# 子类无法继承父类的私有属性和私有方法
print(grand.__money)  # 无法访问实例属性__money
grand.__info_print()