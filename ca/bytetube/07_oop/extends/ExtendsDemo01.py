# 父类A
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


#子类默认继承父类的所有属性和方法
# 子类B
class B(A):
    pass


result = B()
result.info_print()  # 1