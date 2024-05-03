#Range
# range()
# range functions returnes a sequence of numbers
# starting from 0 by default
# increments by 1 by default
# and stops before the specified number.
#a range always stops imideate before the stop condition
# range(start,stop,increment)

#A range by for to output 1-10

for i in range(10): #range(stop)
    print(i) #the start is 0 and the increment is 1 by default
print("END")

for i in range(2,10): #range(start,stop)
    print(i)
print("END")

for i in range(2,10,2): # range(start,stop,increment)
    print(i) #its also the program to output even number
print("END")

for i in range(1,10,2):
    print(i) #its also the program to output odd number