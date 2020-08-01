
from abc import ABC,abstractmethod


class Payment(ABC):
    @abstractmethod
    def make_payment(self):
        pass


#real obj
class Bank(Payment):
    def __init__(self):
        self.account = None
        self.card = None


    def _has_funds(self):
        return True


    def _get_account(self):
        self.account = self.card
        return self.account


    def set_card(self,number):
        print("dbit card no."+(number) + "accepted" )

    def make_payment(self):
        if self._has_funds():
            print("payed")
        else:
            print("rejected")


#proxy
class Debit_card(Payment):

    def __init__(self):
        self.bank = Bank()#目标对象：被代理对象 real obj

    def  make_payment(self):
        number = input("enter your dbit card #")
        self.bank.set_card(number)
        return self.bank.make_payment()


class Client:

    def __init__(self):
        print("buy stuff")
        self.debitcard = Debit_card()

    def buy(self):
        self.debitcard.make_payment()



client = Client()
client.buy()

