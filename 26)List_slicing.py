#List_slicing
#Smiliar like string slicing
# list_name[starting index : ending index]
marks=[1 , 2 , 3 , 4 , 5]
print(marks[0:2])#[1 , 2]
#it will print until 2 not including 2 -> Ending index is not included

print(marks[ : 3]) #is same as [0:3]
print(marks[2: ]) #is same as [2: len(marks)]
print(marks[-3 : -1])#[3,4]