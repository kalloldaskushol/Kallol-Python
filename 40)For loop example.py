#For loop example

num = [1,2,3,4,5.1111]

for val in num:
    print(val)

tuple = (1,2,3,4,5,6,7,8,9.00 )

for num in tuple:
    print(num)

str = "Kallol das Kushol"

for char in str:
    if( char == "d"):
        print("d is found")
        break
    print(char)
else:
    print("END OF LOOP")# It will executive if the loop is succesfully finished


list = [1,4,9,16,25,36,49,64,81,100]
#print the elements using for loop

for i in list:
    print(i)

list = [1,4,9,16,25,36,49,64,81,100]
#Find the value is in the list or not

x = int(input("Enter the number:"))#the search will be down one to one
                                   #means 1st it will check idx 0 then 1 then 2....
                                   #its called linear searching
index = 0
for i in list:
    if (x == i):
        print("x is FOUND in index",index)
        break
    index +=1
else:
    print("NOT FOUND")