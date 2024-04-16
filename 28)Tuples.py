#Tuples
#Tuples are smililer like list but they are immutable
#A build-in data type that lets us to create immutable sequences of values
#Tuples are in perintesis ()
#the value of a element can't change because its immutable

tuple = (1,2,3,4)
print(tuple)
print(type(tuple))
print(tuple[0])#1
print(tuple[2])#3
print(tuple[0:2])#(1,2)
"""
tuple[0] = 5
its not possible because its immutable
"""

#tuple.index(elemnet) -> outputs the index number of the element
#tuple.count(element) -> outputs the total

tup0 = ()
print(tup0)
print(type(tup0))
#Its a empty Tuple

tup1=(1,)
print(tup1)
print(type(tup1))
#if their is one element then it should be seperated by comma(,)
#or else it will identified as a value to the variable

