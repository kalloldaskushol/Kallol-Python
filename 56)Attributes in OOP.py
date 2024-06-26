# Attributes in OOP
# The data we store in the class or object like veriables(name,id,marks) are called Attributes

"""
their are two type of Attributes
1.Class Attribute
2.Instance Attribute or Object Attribute

Class Attribute is mainly that veriable which is defined single time and same for every object
like university name which will be same for all and we define it once so that we could save memory & remove the hastle

Instance Attribute or object Attribute is that Attribute or veriable which are defined in the constructor
self.abc these are mainly object Attribute

"""

class Student():
    
    University = "Leading University" # Class Attribute
    def __init__(self,name,id):
        self.name = name # Object Attribute
        self.id = id

s1 = Student("kallol",6)
print(s1.name ,s1.id, s1.University) 
# If their are 2 attibutes in a program and the have the same name the obj attribute will be exicute