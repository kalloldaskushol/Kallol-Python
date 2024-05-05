#Range_example

#WAP to print 1-100 using for and range 
i = 1
for i in range(1,101,1):
    print(i)


#WAP to print 100-1 using for and range 
i = 1
for i in range(100,0,-1):
    print(i)


n = int(input("Enter the value of n:"))
i = 1

for i in range(1,11,1):
    print(n*i)


#WAP to find the sum of first n numbers

n = int(input("Enter the value of n for sum:"))
sum = 0
for i in range(1,n+1,1):
    sum = sum + i
print("total sum =",sum)

#same qus by while loop

n = int(input("Enter the value of n for sum:"))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print("total sum =",sum)


#Find factorial by while loop
n = int(input("Enter the number you want to find fact."))
factorial = 1
i = 1
while(i <= n):
    factorial = factorial * i
    i = i+1
print("Factorial",factorial)


#Find factorial by for loop
n = int(input("Enter the number you want to find fact."))
factorial = 1
for i in range(1,n+1,1):
    factorial = factorial * i
print("Factorial",factorial)