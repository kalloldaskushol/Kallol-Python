#Function
#Block of statements that perform a specific task
"""
SYNTEX->

def func_name ( peramter1 , perameter2 ):
    working task
    retuen value

"""
"""
Function call:
func_name(argument1 , argument2)
"""
#Peramiter -> are like veriable 
#Argument -> means putting perticuler values in the previous  perameter

#Average of 3 numbers

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum / 3
    print(avg)
    return avg #print is must otherwise we wont get any output

calc_avg(2,4,6)
calc_avg(100,200,300)

#Sum calculator
def sum_calc(a,b):
    sum = a+b
    print(sum)
    return sum

sum_calc(1,2)

#OR

def sum_calcu(a,b,c):
    sum =  a+b+c
    print(sum)
    return sum

sum_calcu(1,2,3)




def print_hello():  #perentesis can be empty also
    print("HELLO WORLD")
    return 0

print_hello()
print_hello()

def hello():
    print("hello")

output = hello()
print(output) #it will return none