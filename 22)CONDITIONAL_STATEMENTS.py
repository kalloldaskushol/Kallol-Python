# CONDITIONAL STATEMENTS
# if-elif-else(SYNTAX-RULES OF WRITING)
# if(CONDITION) :
#     STATEMENT1 (after if-elif-else there should be a 4space gap which is called indentation)
# elif(CONDITION) :
#     STATEMENT2
# else:
#     STATEMENT

age = int(input("Whats your age: "))
if(age >= 18):
    print("Can vote & drive")
else:
    print("Can't vote")


age1 = int(input("Whats your age: "))
if(age1 >= 18):
    print("Can vote")
if(age1 >= 20):
    print("Can't vote")
else:
    print("ABC")
#in this case we haved used multiple (if) with out (elif) thats why both of the condition will be checked but if we had used if_elif in that case if the first case was true 2nd condition would not be chacked