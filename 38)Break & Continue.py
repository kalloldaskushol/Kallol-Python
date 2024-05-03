#Break & Continue
#Break is used to terminate/stop the loop when encountered

#we want to print 1-10 but we want it to stop in 5

i = 1
while(i <= 10):
    print(i)
    if i == 5:
        break
    i = i + 1
print("End of loop")

#Continue terminates execution in the current iteration & continues execution of the loop with the next iteration
#Continue is used like skip
#if we want to skip a value then we use continue
#then it will output all the rest without that perticular

#we want to print 1-10 without 5

i = 1
while i <= 10:
    if (i == 5):
        i = i + 1 #if i = 5 then increase i
        continue #and skip it - 5 
    print(i)
    i = i + 1

#Print odd numbers in 1-10
i = 1
while(i <= 10):
    if i % 2 == 0:
        i += 1 #if modulo turns into 0 then i will be increased
        continue#which of the value outputs modulo 0 thats even and it will be skiped
    print("odd",i) 
    i +=1

#Print even numbers in 1-10
i = 1
while(i <= 10):
    if (i%2 != 0):
        i +=1 #if modulo is not equal to 0 then i will increased 
        continue #which of the value outputs modulo not equals to 0 thats odd and it will be skiped
    print("even",i)
    i += 1

    