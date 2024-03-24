"""
Make a program to find the grade of a student
"""
marks = int(input("Input Your mark :"))
if(marks >= 90 and marks<=100):
    print("A")
elif(marks >=80 and marks<90):
    print("B")
elif(marks >=70 and marks<80):
    print("C")
elif(marks >=60 and marks<70):
    print("D")
elif(marks >=50 and marks<60):
    print("E")
else:
    print("F")
    