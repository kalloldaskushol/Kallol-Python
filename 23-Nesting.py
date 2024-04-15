#Nesting
#if in a if

age = int(input("Enter your age="))
if(age >=18):
    if(age > 80):
        print("Your age is to high you can't drive")#age is greater then 80 the he can't drive
    else:
        print("You can drive")
else:
    print("You Can't Drive your under aged")
#This program denptes that if someones age is greater then 80 then he can't drive
#age 18-79 he can drive
#if the age is less then 18 then he is under aged