"""
Practice_2
print output for
A = 5 & G = M
A = 2 & G = F
"""
A = int(input("A ="))
G = input("F/M =")
if ((A == 1 or A == 2) and G == "M"):
    print("Fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("Fee is 200")
elif(A == 5 and G == "M"):
    print("Fee is 300")
else:
    print("No Fee")
"""
in 1st case 3rd condition is applied
in 2nd case their is a or function so the equation 0 or 0 or 1 which ends with the result 1/True
"""