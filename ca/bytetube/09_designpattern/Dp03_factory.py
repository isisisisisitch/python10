
#db:oracle,mysql,mangodb...
#interface:标准

from abc import ABC,abstractmethod


class data_base(ABC):

    @abstractmethod
    def connetion(self):
        pass


class mysql_server:
    def connetion(self):
        return ("mysql db connetion")



class Oracle_server:
    def connetion(self):
        return ("Oracle db connetion")


class db_factory:
    def get_db_connetion(self,db):
        return db.connetion()


factory = db_factory()
print(factory.get_db_connetion(mysql_server()))
print(factory.get_db_connetion(Oracle_server()))