class Dog(object):
    tooth = 10


cado = Dog()
tony = Dog()

# 修改类属性
# Dog.tooth = 12
# print(Dog.tooth)  # 12
# print(cado.tooth)  # 12
# print(tony.tooth)  # 12

# 不能通过对象修改属性，如果这样操作，实则是创建了一个实例属性
cado.tooth = 20
print(Dog.tooth)  # 10
print(cado.tooth)  # 20
print(tony.tooth)  # 10