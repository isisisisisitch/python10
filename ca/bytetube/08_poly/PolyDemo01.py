class Dog(object):
    def work(self):  # 父类提供统一的方法，哪怕是空方法
        print('eat and sleep...')


class ArmyDog(Dog):  # 继承Dog类
    def work(self):  # 子类重写父类同名方法
        print('execute tasks...')


class DrugDog(Dog):
    def work(self):
        print('find drugs...')


class Person(object):
    def work_with_dog(self, dog):  # 传入不同的对象，执行不同的代码，即不同的work函数
        dog.work()


ad = ArmyDog()
dd = DrugDog()

person = Person()
person.work_with_dog(ad)
person.work_with_dog(dd)