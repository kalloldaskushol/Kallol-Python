#File I/O
"""
File I/O (Input/Output) in Python involves reading from and writing from to files.

types of all files
1)Text files : .txt , .docx , .log etc
2)Binary files : .mp4 , .mov , .png , .jpg etc

Open a file for reading
file = open('example.txt', 'r')

Open a file for appending (this will create a new file if it doesn't exist)
file = open('example.txt', 'a') [append will write something from the last line]
"""

#We have to open a file before reading or writing

file = open("demo.txt","r")
# data = file.read()
# print(data)
print(file.read())
print(type(file.read()))
file.close()

#Character and there meanings 
"""
r -> open for reading (default)
w -> open for writing
x -> create a new file and open it for writing
a -> open for writing, appending to the end of the file if it exists
b -> binary mode = [file = open("file_name","wb)]
t -> text mode (default) = [file = open("file_name","rt")]
+ -> open a disk file for updating such as reading and writing [r+ / w+ means to read and write together]
"""

#Reading a file
f = open("demo.txt","r")
print(f.read(10))#it will output 1st 10th character
print(f.readline()) #in this case the line will start after the 10 char bcz 1st 10 character is called previously and IO function works as a pointer
f.close()

f = open("demo.txt","r")
print(f.readline()) #when we use readline function then we find a extra line which is because before every new line there is a \n
print(f.readline()) #now extra space will not be created but if we print next line again then it will print next line as a space line
f.close()


#Writing a file 

#Open a file for writing (this will create a new file or truncate[delete present data and become a blank sheet] an existing file)
# file = open('example.txt', 'w')

f = open("demo2.txt" , "w")
f.write("using write function to write \nit will dlt previous text")
#if file name does not matches then it will make a file and then write

#If we want to add text at the bottom but not want to erase old text then we will use append

f = open("demo2.txt","a")
f.write("we are using append to write")#it will start where the writing is stops means on the last pointer

# https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function

'''
 The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream/pointer is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file. in this the file doesn"t erases

 ``w''   Truncate[erase] file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated[erased].  The stream is positioned at
         the beginning of the file.
 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
'''

#in r+ mode the file stays the pointer starts from the start
#in w+ mode the file is erased
#in a+ mode the file stays and the pointer starts from the end

#With syntex
#Opening a file and giving him a name it will be in a indented part and it will be closed by the closing of indentetion
print("START NEW FILE")
with open("demo.txt" , "r") as g:
    # data = g.read()
    # print(data)
    print(g.read())

with open("demo2.txt","a+") as h:
    h.write("\nhello we are using with")
    #the a+ is writen after the write function ends in code line 53
    #we are also using append(CODE LINE:59) in previous thats why the previous writing is coming on the last

#if we want to delete a file by python

"""
if WE want to delete a file using python then we have to use [os module]
Module is like  code library such as we use stdio.h in C.
It's written by another programmer that generally has a functions we caan use

SYNTEX
import os
os.remove(filename without cotetion)
"""
import os
#os.remove(demo.txt)