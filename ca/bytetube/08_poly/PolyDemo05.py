class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


cado = Dog()
result = Dog.get_tooth()
print(result)  # 10