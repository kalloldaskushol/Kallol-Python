#Practice_12
#Create a new file name "practice.txt" using python. Add the following data in it:
"""
Hi everyone
we are learning file I/O
using java 
i like programming in Java.
"""

with open("52)Practice.txt" , "w+") as f:
    f.write("Hi everyone\nwe are learning file I/O\nusing java ")
    f.write("\nI like programming in java")

#WA function that replaces all occurrences of java to python

def change_java_python():
    with open("52)Practice.txt","r") as f:
        data = f.read()
    new_data = data.replace("java","Python")
#1st we read the file and add a new veriable called new_data that uses replace function which will replace java to python
    with open("52)Practice.txt","w") as f:
        f.write(new_data)
#we write the file and use write function which will add full new data to the file
#the new_data consists full writing not only python

change_java_python()

#WA function which will  searcch if the word (learning) exists in the file or not

def find_learning():
    word = "learning"
    with open("52)Practice.txt" , "r") as f:
        data = f.read()
        if(data.find(word) != -1):
#If the substring is not found, find() returns -1.
#In the context of find(), -1 explicitly means that the substring does not exist in the string being searched.
            print("Found")
        else:
            print("Not Found")

find_learning()

#WAF to find in which line of the file does the word "learning" occurs first.Print -1 if word not found.

def find_line_Numb():
    word = "Python"
    data = True
    line_Num = 1
    with open("52)Practice.txt" , "r") as f:
        while (data):
            data = f.readline()
            if(word in data): #works like code_line 34 -> it means finding learing in data which is the readline
                print(line_Num)
                return
            line_Num = line_Num + 1
    return print("-1")

find_line_Numb()


#WAP which will from a file containing numbers separated by comma & print the count of even numbers

with open("53)Practice2.txt","w") as f:
    f.write("1,2,4,55,86,76")

count = 0
with open("53)Practice2.txt","r") as f:
    data = f.read()
    numbers = data.split(",")
    for value in numbers:
        if(int(value) % 2 == 0):
            count += 1

print("the number of even number is",count)