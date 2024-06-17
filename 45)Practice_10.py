#Practice_10

#WAP to print the lenth of a list

cities = ["Sylhet","Dhaka","chittagong","Rajshahi","Borishal"]
heros = ["Ironman ","Spiderman ","Batman ","Kallol "]

def print_lenth(list):
    print(len(list))
    return print_lenth

print_lenth(cities)
print_lenth(heros)

#WAP to print list elements in a single line

print(heros[0],end ="")
print(heros[1],end ="")
print(heros[2],end ="")

#WAP to print list elements in a single line using function

def print_list(list):
    for item in list:
        print(item,end = " ")
    return print_list

print_list(cities)
print()


#WAP to find the factorial of n using function

def calc_fact(n):
    fact = 1
    for i in range(1,n+1,1):
        fact = fact * i
    print(fact)
    return calc_fact

calc_fact(5)
calc_fact(8)

#WAP to convert USD to TAKA

def converter(USD):
    TAKA = 135 * USD
    print(USD ,"/- USD =", TAKA ,"/- TAKA")
    return TAKA

converter(120)

def odd_even(n):
    if (n % 2 == 0):
        print("EVEN")
    else:
        print("ODD")
    return odd_even

odd_even(2)
odd_even(5)