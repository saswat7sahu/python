class Employee:
    #class variable 
    total_employee=0
    #constructor
    def __init__(self,id,name,role):
        self.id=id
        self.name=name
        self.role=role
        Employee.total_employee+=1
    
    def __str__(self) :
        return"employee id is {} role {} and name is{}".format(self.id,self.role,self.name)
    def __del__(self):
        Employee.total_employee-=1
suresh=Employee(1,"pp","Dwvops") 
print(Employee.total_employee)
print(suresh.id)
print(str(suresh))
del suresh


        
        