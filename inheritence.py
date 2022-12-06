# Inheritance concept

# Way of forming new classes using classes that are already defined
# lets create a base class
class Animal():
    def __init__(self):
        print ("Animal Created") 

    def who_am_i(self):
        print ("i am an animal")
    def eat(self):
        print ("i am eating")        

myanimal=Animal()
myanimal.who_am_i()
myanimal.eat()
myanimal

# lets create a derived class where we will be inheriting some of the features from the base class animal
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print ("Dog Created")
#     # overriding eat method of Animal Class 
#     def eat(self):
#         print ("I am a dog eating")
#     def bark(self):
#         print ("i am barking")  
# mydog=Dog()
# mydog
# mydog.bark()
# mydog.who_am_i() 
# mydog.eat()

class Employee():
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount=Employee.empcount+ 1

    def displayEmployeeInfo(self):
        print ("Employee Name",self.name,"Employee Salary",self.salary)

    def employee_count(self):
        print ("Employee Count",Employee.empcount)

emp_1=Employee("Bhawesh",2000)
emp_1.employee_count()
emp_2=Employee("Saumya",5000)
emp_2.employee_count()
emp_1.employee_count()




