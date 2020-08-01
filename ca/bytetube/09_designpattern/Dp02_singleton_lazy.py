class Singleton(object):
    #class attr
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called")
        else:
            print("instance already exist!", self.get_instance())



    @classmethod
    def get_instance(cls):

        if not cls.__instance:
            cls.__instance = Singleton()

        return cls.__instance






s1 = Singleton()
#obj first created: <__main__.Singleton object at 0x10516fcc0>
print("obj first created:", Singleton.get_instance())

#instance already exist! <__main__.Singleton object at 0x10516fcc0>
s2 = Singleton()

