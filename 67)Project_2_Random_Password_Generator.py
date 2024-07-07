#Project_2_Random_Password_Generator

import random
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)

pass_len = int(input("Enter the length of the password:"))
char_value = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(pass_len):
    password = password + random.choice(char_value)

print("Your Password is:",password)

# If we want to create the pass using a list 
password_list = "[]" . join ( [random.choice(char_value) for i in range (pass_len) ] )
print("your list password:",password_list)