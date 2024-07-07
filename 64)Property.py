# Property

#We use @property decorator on any method in the class to use the method as a property
# Such as we want to make a veriable which is dependent on other veriable,
# in the case if we just only normally code it then the the function will run
# but if in another line we change the data then the previous value will be counted insted of new one.
# In this case we use @property method so that it converts to a value that will change along with the value given to it changes

class Percentage():
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

        self.percentage = str((self.phy+self.chem+self.math)/3) + "%"

s1 = Percentage(98,97,99)
print(s1.percentage)

#now if we change the value of physics then

s1.phy = 86
print(s1.phy)
print(s1.percentage) #The percentage value didn't changed because it was defined along with the student object

#if we write the code with @property decoretor then

class Student:
    def __init__(self,ban,eng,bgs):
        self.ban = ban
        self.eng = eng
        self.bgs = bgs

    @property
    def calc_percentage(self):
        return print( str((self.ban+self.eng+self.bgs)/3) + "%")

s2 = Student(90,92,96)
s2.calc_percentage
s2.bgs = 50
s2.calc_percentage