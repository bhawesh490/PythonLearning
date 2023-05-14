# Object Oriented Programming Language concepts

# Object Oriented Programming Allows us to create our own objects that have methods and attributes



# 1-class 
# 2-Object  
# 4-Methods 
# 5-Attributes and properties is the characteritics of the object
# Properties are special types of attributes 

# Syntax:
# functions and variables are stores in lowercase 
# while classes are stored in Camelcase letters or in Upper case

# Attributes and Methods Difference


# class NameOfClass():
#     def __init__(self,param1,param2):
#         self.param1=param1 
#         self.param2=param2
    
#     def some_method(self):
#         Perform some action
#         print (self.param1)    


# Lets create a simple class 

# class Sample():
#     pass
# my_sample=Sample() #instance of the class which is an object
# list=[1,2,3]
# print (type(my_sample))
# print (type(list))


# class Dog():
#     def __init__(self,breed): #Defining the attibutes/Characteristics of the dog
#         self.breed=breed
# my_dog=Dog(breed='Lab')
# print (type(my_dog))  
# print (my_dog.breed)


# class Dog():
#     def __init__(self,breed,name,spots): #Defining the attibutes/Characteristics of the dog
#         self.breed=breed
#         self.name=name
#         self.spots=spots 

# my_dog=Dog(breed='Lab',name='Blackie',spots=True) #Creating instance of the call which is an object
# print (my_dog.breed)
# print (my_dog.name)
# print (my_dog.spots)

# Global Attribute 

# class Dog():
#     # class object attribute
#     # same for any Instance of a class
#     species="Mammel"

#     def __init__(self,breed,name,spots):
#         self.breed=breed
#         self.name=name
#         self.spots=spots 

# # creating instance of the class Dog() my_dog which is an object
# my_dog=Dog(breed='Lab',name='Jakie',spots=True)
# print (my_dog.species) #here this is an attribute of class object
# print (my_dog.breed)
# print (my_dog.name)
# print (my_dog.spots)

# Methods are Like Operations and actions
# Atrributes dont use parenthesis
# Method uses parenthesis()

# class Dog():
#     # class object attribute
#     # same for any Instance of a class
#     species="Mammel"

#     def __init__(self,breed,name,spots):
#         self.breed=breed
#         self.name=name
#         self.spots=spots 

#     # Operations/Actions-->Methods
#     def bark(self,number):
#         print ("Woof My name is {} and my number is {}".format(self.name,number))


# # creating instance of the class Dog() my_dog which is an object
# my_dog=Dog(breed='Lab',name='Jakie',spots=True)
# print (my_dog.species) #here this is an attribute of class object
# print (my_dog.breed)
# print (my_dog.name)
# print (my_dog.spots)
# my_dog.bark(10) #Method takes parethesis

# # Lets create a new class now
# class Circle():
#     # Class object attribute
#     pi=3.14 
#     def __init__(self,radius=1):
#         self.radius=radius 
#         self.area=radius*radius*Circle.pi 
#         # or 
#         # self.area=radius.radius.self.pi
#     # Method
#     def Circumference(self):
#         return self.radius*Circle.pi*2 
#         # or
#         # return self.radius.self.pi*2   
# my_circle=Circle(2)
# print (my_circle.area)
# print (my_circle.Circumference())     
# print (my_circle.radius)
# print (my_circle.pi)      


# Create a class for dictionary parsing
# 1-Write a function to read all the key 
class Dictionary_parse():

    def __init__(self,a):
        self.a=a

    def  read_key(self):
        if type(self.a) is dict:
            return  self.a.keys()
        else:
            return "its not a dictionary"    

my_dict=Dictionary_parse([1,2,3])
print (my_dict.read_key())           




# learning




