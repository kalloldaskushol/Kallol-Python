#Function_Types
#there are 2 types of function
"""
1.Build-in function ->
    print()
    type()
    range()
    len()

2.User defined function ->
    the function which is defined by the user
"""

#if we want to run a function without giving perameter then we have to give them default value

def cal_product(a=1 , b=1):
    cal_product = a*b
    print(cal_product)
    return cal_product

cal_product()

#If we want to take one value from the user then we have to make default value last one
#default value starts from the right

def calc_product(a,b=1):
    product = a * b
    print(product)
    return cal_product

calc_product(2) 