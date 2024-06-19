#Practice_11

#WA recursion program to print the value n-0
def print_n(n):
    if (n == 0):
        return
    print(n)
    print_n(n-1)

print(print_n(5))
print(print_n(10))
#in this case it outputs none on the last because we have use print function to call the function but didnt give any return value
#thats why when the value comes to 0 then there is nothing to print thats why it prints none

# The function print_n(n) is called with n = 5.
# The function prints 5, then calls itself with n = 4.
# This continues until n reaches 0, at which point the function simply returns (without printing anything because of the base case if (n == 0): return).
# After the base case is hit, each recursive call completes and returns to the previous call, all the way back to the initial call.
# Since the function doesn't explicitly return a value, Python returns None by default.
# When you use print(print_n(5)), the print function prints the return value of print_n(5), which is None.

print_n(5)
#if we use call like this then it wont return none because we havn't used an extra print function thats why when the base case will enter the func will brack without printing

print("END")
#WA recursion program to print the value 0-10

def print_m(m):
    if (m == 11):
        return
    print(m)
    print_m(m+1)

print_m(0)

print("END")

#WA recursion program to calculate the sum of n natural number

def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n # n = 5 -> (1+2+3+4)+5(n)

print(calc_sum(5))
print("ENDDDD")

#write a recursive function to print all elements in a list.
#Use list & index as perameters

def print_list(list,index = 0):
        if (index == len(list)):
            return
        print(list[index])
        print_list(list,index+1)

    
fruits = ["mango","litchi","apple","bananna"]

print_list(fruits)