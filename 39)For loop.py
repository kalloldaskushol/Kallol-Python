#For loop
#for loops are used to sequential traversal(1st index 0 then idx 1 then idx 2...)
#for traveling in a list,tuple,string etc

"""
SYNTEX:

string = "kallol das kushol"
for char(we can take it by us,it doesn't need to be mentioned previously) in string:
    work

    
for loop with else
we use else to notify thats loop is fully done and its now stoped.
if we dont use else rather we use print statement in the end then it will always output the print statement it doesn't metter loop is fully executed or not
we mostly use (else) when we use break and continue in a for loop

SYNTEX
list = [1,2,3,4,5]
for elements in list:
    if (elements == 4 ):
        print( "4 is found" )
        break
    work
else
    work -> it will work when the loop is totally finished

"""

list = [1,2,3,4,5]
for ele in list:
    print(ele)

###############
list = [1,2,3,4,5,6]
for ele in list:
    if (ele == 4):
        print("4 is found")
        break
    print(ele)
print("end but loop is not completed")

list=[1,2,3,4,5,6,7,8,9]
for ele in list:
    if ele == 6:
        break
    print("i =",ele)

list=[1,2,3,4,5,6,7,8,9]
for ele in list:
    print("i` =",ele)
    if ele == 6:
        break

#both are looking similer but they aren't same
#in the first one, the last output will be 5 bcz when the ele = 6 the break will exicute and it wont print the rest
#in the second one,the last output will be 6 bcz after printing 6 the if statement will be checked and then the break will exicute and it wont print the rest