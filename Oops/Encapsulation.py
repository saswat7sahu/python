#Encapsulation is oops concept where we hide the data .so that out side of class we can't access.
#so we declare the instace variable as private .
class laptop:
    def __init__(self,name,ram) :
        self.__name=name
        self.__ram=ram
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,name):
        self.__name=name
    @property
    def ram(self):
        return self.__ram
    @ram.setter
    def ram(self,ram):
        self.ram=ram

hp=laptop("hp",8)
print(hp.ram)
