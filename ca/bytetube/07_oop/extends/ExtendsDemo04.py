class Master(object):
   def __init__(self):
    print("master init")
    self.kongfu = '[Master method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')



class School(object):
    def __init__(self):
     print("School init")
     self.kongfu = '[bytetube method]'

    def make_cake(self):
        print(f'{self.kongfu} to make cake')


# 独创配方
class Prentice(School, Master):
   def __init__(self):
       print("Prentice init")
       self.kongfu = '[original method]'

   def make_cake(self):#重写 override
        print(f'{self.kongfu} to make cake')


prentice = Prentice()
print(prentice.kongfu)
prentice.make_cake()

#(<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>)
print(Prentice.__mro__)