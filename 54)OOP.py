#Object Oriented Programming
"""
To map with real world scenarios,we started using objects in code
this is call object oriented programming(OOP)

Object-Oriented Programming (OOP) is a programming paradigm that,
organizes software design around data, or objects, rather than functions and logic.

Objects -> An instance of a class. It contains real values instead of variables.

Class -> A blueprint for creating objects.
It defines a set of attributes and methods that the created objects will have.

Attributes (Properties): These are the data stored inside an object.
For example, a Car object might have attributes like 'color', 'make', and 'model' .

Methods (Functions): These are the functions defined inside a class that describe the behaviors of the objects.
For example, a Car class might have methods like start(), stop(), and drive().


"""
#Class is like a classroom & object are like students in the class

"""
SYNTEX of creating a class =
class Class_name:        class name starts with capital letter
    information
    name ="kallol"
    id=12
    instritution = "LU"

    
SYNTEX of creating a object =

1st object->

s1 = Class_name()
print(s1.name)
print(s1.id)

"""

class Student():
    name = "Kallol Das Kushol"
    id = 182410012101006
    ins="LU"

s1 = Student()
print(s1) #printing the location of the object
print(s1.name) 
print(s1.id)
print(s1.ins) 

# s2 = Student()
# print(s2) #printing the location of the object
# print(s2.id)
# print(s2.name)
# print(s2.ins) 

#it will give the same output bcz,
#its the blueprint and all the output will have to follow it