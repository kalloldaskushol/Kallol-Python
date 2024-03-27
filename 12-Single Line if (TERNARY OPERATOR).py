#Single Line if / TERNARY OPERATOR 
#variable = value1 if condition else value2
food = input ("whats the Food :")
eat = "yes" if food == "cake" else "no"
print(eat)
#statement1 if condition else statement2
food2 = input("Food2 : ")
print("sweet") if food2 == "cake" or food2 == "jalebi"  else print("not sweet")

#Clever if / ternary operator
#variable = (false_this value , true_this value) [CONDITION]

age = int(input("Whats your age: "))
vote = ("yes you can vote!" , "Sorry! you cant vote~") [age <=18 ]
print(vote)

sal = float(input("salary = "))
tax = sal * (0.1 , 0.2) [sal >= 50000]
#0 - 50k -  10%
#50k ++ - 20%
print(tax)