#Indexing
#indexing means the positioning of a charecter in a string
#indexing always starts from the left and the starting charecter is 0
#we have to use square beackets
#we also can't modify charecters by this function
name = "Kallol Das Kushol"
print(name[0])
print(name[2])
print(name[9])
print(name[10])#space is also denoted

#Slicing
#Accessing parts of a string

name = "Kallol Das Kushol"
print(name[1:4])
#the 4th charecter is o but it will return output without 4th one means the last 3rd one which is l
print(name[0:])#0 to last
print(name[ :len(name)])
#len(name) denotes the last charecer in the string

#string slicing also can be start from backwords
#its called the negative slicing
#in this case numbering starts from the last letter which is denoted as (-1)

a = "apple"
"""
a -5
p -4
p -3
l -2
e -1
"""
print(a[-3:-1])
#the output will be till -1 