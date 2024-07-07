# Mathods in OOP
# We can store 2 things in a class they are data(attributes) and mathods
# Mathods are functions that belong to objects
# if we write a function in a class then it means a function

class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self): #Mathod
        print("welcome!",self.name,"we are learning mathod...")


s1 = Student("kallol",99)
s1.welcome() # Calling mathods

# Create student class that takes name & marks of 3 subjects as arguments in constructors
# Then create a method to print the average

class Student_Practice():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 

    def avg(self):
        sum = 0
        for i in self.marks:
            sum = sum + i
        print("Hi!",self.name,"The average of the marks is",sum/3)

s2 = Student_Practice("kallol",[98,99,100])
s2.avg()


# In methods we have to give a (self) parameter but if we want a function without a self parameter
# Then we use a Decorator which is (@staricmethod)
# which allows us to use a function without parameter
# it works on class level

class New_student():
    @staticmethod
    
    def Hello():
        print("Hello world")

s3 = New_student()
s3.Hello()