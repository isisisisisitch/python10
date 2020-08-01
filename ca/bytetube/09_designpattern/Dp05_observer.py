
#被观察者
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self,observer):
        self.__observers.append(observer)

    def notify(self,*args, **kwargs):
        for observer in  self.__observers:
            observer.notify(self,*args, **kwargs)


class Observer1:
    def __init__(self,subject):
        subject.register(self)

    def notify(self,subject,*args, **kwargs):
        #
        print(type(self).__name__,': got', args ,'from', subject)


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args, **kwargs):
        print(type(self).__name__, ': got', args, 'from', subject)



subject = Subject()

#Observer1 : got ('hello!',) from <__main__.Subject object at 0x1084471d0>
observer1 = Observer1(subject)
#Observer2 : got ('hello!',) from <__main__.Subject object at 0x1084471d0>
observer2 = Observer2(subject)

subject.notify("hello!")