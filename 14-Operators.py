#Operators
#An operator is a symbol that performs a certain operation between operands
# Types of operators
# Arithmetic Operator(+ - * / % **)

a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)# division will always bring a output as a float 
print(a%b)# Modulo Operator used to calculate Remainder
print(a ** b)# a^b


# Relational / Comparison Operators (== != < > <= >=)
a = 50
b = 20
print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b) #True
print(a <= b) #False
print(a < b) #False

#assignment operators(= += -= /= %= **=)
num = 10
num = num + 10 # num =10+10=20
print("num = ", num)
num += 10 #num = num +10 =20+10=30
print("num += = ", num)
num -= 5 #num =num - 5 = 30-5 =25
print("num -= = ", num)
num *= 5  #num = num * 5 = 25*5=125
print("num *= = ", num)
num /= 5 #num = num/5 = 125/5 =25
print("num /= = ", num)
num %= 5 #num = (num % 5) = 25%5=0
print("num %= = ", num)
num **=0 #num = 0 to the power 0
print("num **= = ", num)

#logical operators (NOT , AND , OR)
a= 50
b= 30
print (not False)
print(not (a > b))
print(a and b)#When using the and operator, Python returns the second operand if the first operand is truthy. In this case
print(a or b)#When using the or operator, Python returns the first operand if it is truthy