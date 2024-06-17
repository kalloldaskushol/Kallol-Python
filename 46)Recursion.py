#Recursion
#When a function calls itself repeatedly
#its kind of loop
#but using a function
#in this case in the function end their is a code written which will call the next value and run the function by itself
#In recursion there have to be a case where the recursion will stop otherwise it will become infinity
#the stop case is build with the help of return and conditional statement
#it is called BASE CASE

#WAP by recursion which will output numbers from 1-5

def show_frontwise(n):
    if (n == 6):
        return 0 #BASE CASE
    print(n)
    show_frontwise(n+1)#calling by the function

show_frontwise(1)

print("END")
#WAP by recursion which will output numbers from 5-1

def show_backwise(n):
    if(n == 0):
        return 0
    print(n)
    show_backwise(n-1)

show_backwise(5)

print("END")


#if we add print funtion and try to write something then it will print everytime

def show_backwise_hello(n):
    if(n == 0):
        return 0
    print(n)
    print('start') #it will exicute before calling next function
    show_backwise_hello(n-1)
    print("HELLO") #it will exicute after calling next function

show_backwise_hello(5)