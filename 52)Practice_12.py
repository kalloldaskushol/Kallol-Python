#Practice_12
#Create a new file name "practice.txt" using python. Add the following data in it:
"""
Hi everyone
we are learning file I/O
using java 
i like programming in Java.
"""

with open("Practice.txt" , "w+") as f:
    f.write("Hi everyone\nwe are learning file I/O\nusing java ")
    f.write("\nI like programming in java")