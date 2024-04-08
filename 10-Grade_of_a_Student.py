"""
Make a program to find the grade of a student
"""
marks = int(input("Input Your mark :"))
if(marks >= 90 and marks<=100):
    print("Grade of the student is -> A")
elif(marks >=80 and marks<90):
    print("Grade of the student is -> B")
elif(marks >=70 and marks<80):
    print("Grade of the student is -> C")
elif(marks >=60 and marks<70):
    print("Grade of the student is -> D")
elif(marks >=50 and marks<60):
    print("Grade of the student is -> E")
else:
    print("Grade of the student is -> F")