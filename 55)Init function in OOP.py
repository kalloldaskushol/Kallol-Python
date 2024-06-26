#init function in OOP

#Constructor
# All classes have a function called __init__() which is always executed
# when the object is being initiated
# in every __init__ function there is a self parameter which is a defualt parameter
# we can also add other parameter after a self parameter
# the self parameter is a reference to the current instance of the  class
# and it is used to access variables that belongs to the class

class Student:
    
    #Default constracter (its always added)
    def __init__(self):
        print(self) #its same as print(s1) it outputs the memory location
        print("Adding new student in database...")

s1 = Student() #It mainly calls the init functions self but all the time its not given it invokes automatically
print(s1)

print("END")
print()
print()


class Room:
    #Parameterized constructor
    def __init__(self,name,marks):
        print("Adding new student in database...")
        self.name = name
        self.marks = marks

s1 = Room("kallol",99.8) # If there are mulltiple constracters then in which the parameter will match that constracter will be worked
print("student.1 =" ,s1.name,s1.marks)

s2 = Room("Shourav",100)
print("student.2 =",s2.name,s2.marks)