#Abstraction & Encapsulation

# their are 4 pillers of OOP
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

# Abstraction -> Hiding the implmentation details of a class and only showing the essential features to the user

# it means hiding the process and only showing the necessary details to the user

#in example, when a car is on rest the  value of the accelerator,Break & Clutch are off which means False in programming
# when we start a car then we have to pull the clutch and press the accelerator means thay will become True only then the car will start
 
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start (self):
        self.clutch = True
        self.acc = True
        print("Car Started....")

car1 = Car()
car1.start()

# In this case when car starts the user is only noticing that car started
# But in the background the clutch and accelerator is being pushed..


# Encapsulation -> Wrapping data and function into a single unit(object)

#it means making a capsule in which data and function are stored


#WA OOP create Account class with 2 attributes - balance & account no


class Bank():
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no
    
    #Debit method
    def Debit(self,ammount):
        self.balance = self.balance - ammount
        print(ammount, "is debited from your account,available balance is",self.balance)
    
    #Credit Method
    def Credit(self,ammout):
        self.balance += ammout
        print(ammout,"is credited on your account,available balance is",self.balance)

    #printing balance method
    def print_balacne(self):
        print("Your Available Balance is TK.",self.balance)
    
account1 = Bank(50000,1234)
print("Your balance TK.",account1.balance)
print("Your Acc_no",account1.account_no)

account1.Credit(10000)
account1.Debit(20000)
account1.print_balacne()