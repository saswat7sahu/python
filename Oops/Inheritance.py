class Person:
    #If the value of a variable is not varied from object to object,
    #  such types of variables are called class or static variables
    total_person=0
    #init is the constuctor.int will execute when a object being created.
    #self” refers to the instance of the class that is currently being used.
    def __init__(self,name,age) :
        self.name=name
        self.age=age
        Person.total_person+=1
    #Destructors are called when an object gets destroyed
    def __del__(self):
        Person.total_person-=1
        print("the object {} deleted".format(self.name))
    #string method use to display all atribute
    def __str__(self):
        return ("name {},age {}".format(self.name,self.age))
class Nationality(Person):
    def __init__(self, name, age,nationality):
        super().__init__(name, age)
        self.nationality=nationality
    def __str__(self):
        prevoius= super().__str__()
        prevoius+= "nationality is {}".format(self.nationality)
        return prevoius
p1=Nationality("sunil",23,"indian")
print(p1)
