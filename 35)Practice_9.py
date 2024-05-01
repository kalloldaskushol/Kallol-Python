#Practice_9
#WAP to enter marks of 3 subjects from the user and store them in a dictionary
#start with an empty distionary & add one by one.use subject name as key and marks as value

marks = {}

x = float(input("Enter your Phy marks:"))
marks.update({"Phy" : x})

y = float(input("Enter your Math marks:"))
marks.update({"Math" : y})

z = float(input("Enter your Chem marks:"))
marks.update({"Chem":z})
print(marks)

#WAP to figure out a way to store 9 & 9.0 as separate values in a set
#Two way one is by using tuple another is by using string

#1st one
values = {
    ("float", 9.0),
    ("int", 9) 
}
print(values)

#2nd one
values2 = {
    9 , "9.0"
}
print(values2)