# Inheritance in OOP
# When one class(Child) derives/Takes the properties & methods of another class(Parent/Base)

"""SYNTEX ->
class Car:      
    print("Hello!") #Base Class

class ToyotaCar(Car): #
    print("")

car1 = ToyotaCar()#we Haved called only ToyotaCar class but because it has inheritanced the Car class thats why onn 1st the base code will be exicuted

# Output ->
# Hello!
# Toyota
"""

class Car():         #Base Class
    colour = "black"

    @staticmethod
    def start():
        print("Starting the car.....")
    
    @staticmethod
    def stop():
        print("Car is being stoped.....")

class ToyotaCar(Car):   #Inheriting the parent class name (Car)
    def __init__(self,Model_name):
        self.name = Model_name


car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")


car1.start() # we are calling start attribute but their is no attribute named start but
# because it has taken the Car class as its parent or base class thats why he can use those attributes to


"""
Type of inheritance ->

1. Single inheritance
2. Multi-level inheritance
3. Multiple inhertance
"""
print()

# 1. Single inheritance is that type of inheritance where there  will be one base and a single child
# The above one is that type of inheritance

# 2. Multi-level inheritance, is basiclly when two or more child derives the base class peoperty

class Multi_Car():#base class
    @staticmethod
    def start():
        print("Car is being started....")
    
    @staticmethod
    def stop():
        print("Car is being stopped....")

class Multi_ToyotaCar(Multi_Car): #Child class but base class for Fortuner
    def __init__(self,model_name):
        self.name = model_name

class Multi_Fortuner(Multi_ToyotaCar): #Child class
    def __init__(self,type):
        self.type = type

carrrr1 = Multi_Fortuner("Petrol")
carrrr1.stop()

#This type of inheritance is called multi level inheritance

# 3. Multiple Inheritance, is that type of inheritance where a child class will take two or more class as its parent/base


class A():
    varA = "Welcome to class A"
class B():
    varB = "Welcome to class B"
class C(A,B): #Child class where A & B both are its base class
    varC = "Welcome to class C"

print()
z1 = C()
print(z1.varC)
print(z1.varB)
print(z1.varA)
