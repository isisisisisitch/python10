class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)

        return cls.instance









s1 = Singleton()
#first obj <__main__.Singleton object at 0x10be3a518>
print("first obj",s1)

s2 = Singleton()
#second obj <__main__.Singleton object at 0x10be3a518>
print("second obj",s2)