#Input
#input() statement is used to accept values from user
"""
input() results always a string
int(input()) - int input
float(input()) - float input
"""
name=input("Enter your name:")
print("Welcome",name)

value = input ("Enter the value:")
print(type (value))

name = input("Enter your name:")
age = int(input("Enter your age:"))
marks = float(input ("Enter your marks:"))
print(type(name))
print(type(age))
print(type(marks))
print("Welcome", name)
print("Your age:",age)
print("Your marks:",marks)