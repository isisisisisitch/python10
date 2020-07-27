# 1. 师父类
class Master(object):
    def __init__(self):
        self.kongfu = '[Master method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')


# 2. 徒弟类
class Prentice(Master):
    pass


# 3. 创建对象徒弟
prentice = Prentice()
# 4. 对象访问实例属性
print(prentice.kongfu)
# 5. 对象调用实例方法
prentice.make_cake()