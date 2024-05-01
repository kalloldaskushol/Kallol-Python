"""
#While_loop_Practice

#WAP to print numbers from 1 to 100
i = 1
while (i <= 100):
    print("i =" , i)
    i += 1

#WAP to print numbers from 100 to 1
i = 100
while (i >= 1): #STOPING CONDITION
    print("j = ",i)
    i-=1

#WAP to print multiplication table of a number n
n = int(input("enter the n ="))
i = 1
while (i <= 10):
    print(n*i)
    i += 1

#WAP to print the elements of the following list using loop
#list = [1,4,9,16,25,36,49,64,81,100]

list = [1,4,9,16,25,36,49,64,81,100] #total = 10
index = 0
while (index < len(list)): #lenth = 10; last index is (lenth - 1) = 9
    print(list[index])
    index+=1
"""
#WAP to search for a number  in this tuple using loop
tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("1,4,9,16,25,36,49,64,81,100 which number"))
i = 0
while( i < len(tuple)):
    if(tuple[i] == x):
        print("Found at index number",i)
    i = i + 1 #it should be in while not in if 