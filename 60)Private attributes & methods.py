# Private attributes & methods
# private attributes & methods are meant to be used only within the class and are not accessible at outside the class
# just use __ before the specific attributes or methods
# It can be used inside the class

class Account():
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #Private
    
    def reset_pass(self): # we can make the method private by using __ 
        del self.__acc_pass #We can use private attributes or methods through class

acc1 = Account("12345","abcde")

print(acc1.acc_no)
# print(acc1.__acc_pass)  -> this will through a error becasue the atrribute is private

acc1.reset_pass()