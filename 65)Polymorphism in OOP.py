#Polymorphism in OOP
# Also known as Operator Overloading
# When the same operator is allowed to have different meaning according to the context

"""
Operators & Dunder functions

Addition -> a+b -> a. __add__ (b)
Subtraction -> a-b -> a. __sub__ (b)
Multiplication -> a*b ->  a. __mul__ (b)
Division -> a/b -> a.truediv____ (b)
Moudulo -> a % b -> a.__mod____(b)
"""

print(1+2) # 3
print("Apna"+"College") # Concatenate
print([1,2,3] + [4,5,6] ) # Merge
print()

#these are already set in python but suppose we want to use plus as our way which is not specified in python
# Then we have to use dunder functions and create our logic to use +,-,*,/

#Suppose we want to addition two complex numbers then we have to dunder function

class Complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def ShowNumber(self):
        print(self.real , "+" , self.img,"i")

    #Complex addition
    def __add__(self,num):
        new_real = self.real + num.real
        new_img = self.img + num.img

        return Complex(new_real,new_img)


num1 = Complex(2,4)
num1.ShowNumber()

num2=Complex(6,8)
num2.ShowNumber()

num3 = num1 + num2 
num3.ShowNumber()