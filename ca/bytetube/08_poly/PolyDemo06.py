class Dog(object):
    @staticmethod
    def info_print():
        print('This is a dog class for creating dog instances.')


cado = Dog()
# 静态方法既可以使用对象访问又可以使用类访问
cado.info_print()
Dog.info_print()