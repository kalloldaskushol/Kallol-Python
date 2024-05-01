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
    if i == 5:
        i = i + 1
        continue # the previous i means skip 5 and become 6 and run... 
    print(i)
    i = i + 1

#Print odd numbers in 1-10
i = 1
while(i <= 10):
    if i % 2 == 0:
        i += 1
        continue# modulo 2 / even will be skiped
    print("odd",i) 
    i +=1

#Print even numbers in 1-10
i = 1
while(i <= 10):
    if (i%2 != 0):
        i +=1
        continue
    print("even",i)
    i += 1