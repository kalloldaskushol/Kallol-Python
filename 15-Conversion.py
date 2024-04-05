#conversion 
#there are two types of conversion
#1.Type conversion-when conversion is done automatically
#2.Type casting - when the conversion has to be done manually

#1.Type conversion
a = 1 #Integer
b = 2.0 #Float
print(a+b)
print(type(b))
#float is a superior data type is this case the integer value is converted to float automatically

#2.Type casting
"""
a = "25"
b = 5
print(a+b)
in the case program willl give output error
so, we have to use type casting - int (a)
"""
a = int("25")
b = 5
print(type(a))
print(a+b)
#the character must be a valid number,aname cannot be converted by type casting
a = 3.14
a = str(a)
print(type(a))