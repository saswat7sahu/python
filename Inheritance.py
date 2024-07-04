class Person:
    total_person=0
    def __init__(self,name,age,id) -> None:
        self.name=name
        self.age=age
        self.id=id
        Person.total_person+=1
    def __str__(self) -> str:
        return "name is {} id {} and age is {}".format(self.name,self.id,self.age)
    def __del__(self):
        Person.total_person-=1
class Student(Person):
    def __init__(self, name, age, id,st_class) -> None:
        super().__init__(name, age, id)
        self.st_class=st_class
    def __str__(self) -> str:
        letters=super().__str__()
        letters+="and study class in {}".format(self.st_class)
        return letters
    def __del__(self):
        return super().__del__()
class Cs_student(Student):
    def __init__(self, name, age, id, st_class,course_type) -> None:
        super().__init__(name, age, id, st_class)
        self.course_type=course_type
    def __str__(self) -> str:
        letters=super().__str__()
        letters+= "and course  is {}".format(self.course_type)
        return letters
Saswat=Cs_student("saswat",22,21,"MCA","python")
print(str(Saswat))