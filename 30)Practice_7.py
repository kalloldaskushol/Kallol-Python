#Practice_7
#WAP to count the number of students with the grade A in the following tuple
# ("C" , "D" , "A" , "A" , "B" , "B" , "A")
grade =("C" , "D" , "A" , "A" , "B" , "B" , "A")
print(grade.count("A"))

#Store the tuple in a list and sort them in a list

grade =["C" , "D" , "A" , "A" , "B" , "B" , "A"]
grade.sort()
print(grade)

#WAP that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

values = input("input some comma-separated nummbers:")
list = values.split(",")
tuple = tuple(list)
print("list:",list)
print("tuple", tuple)