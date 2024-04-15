#List
#list is used for storing multiple values in a single line
#A build in data that stores set of values
#it can store element of multiple types(integers,float,string etc)
marks = [94.3 , 93.5 , 32.6 , 55.3 , 56.3 , "kallol" , "kushol"]
print(marks)
print(type(marks))
print(marks[0])#94.3
print(marks[2])#32.6
print(len(marks))#only the values will be counted


#string are immutable
#on the other hand, lists are mutable
#it means we can change & access list items but we can only access string we can't change their value

str= "hello"
print(str[0])#we can access
"""
str[0] = "k"
we can't change the value
"""

student=["KALLOL" , 21 , 95.6 , "Sylhet"]
print(student[0]) #ACCESS
student[0]="Kushol" #CHANGE

print(student)