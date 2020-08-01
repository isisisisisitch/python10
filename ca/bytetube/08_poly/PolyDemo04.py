class Dog(object):

    def __init__(self):
        self.age = 5

    def info_print(self):
        print(self.age)


cado = Dog()  # Dog()是创建实例对象时所调用的构造方法，内部会自动调用 __init__
print(cado.age)  # 5
print(Dog.age)
cado.info_print()  # 5