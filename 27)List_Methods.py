#List_Methods
list = [3 , 2 , 1]
#list.append(value) -> will add the value in the last new index [1 , 2 , 3 , 4]
list.append(0)
print(list)#[3 , 2 , 1 , 0]

#list.sort() -> sorts in ascanding order [1, 2 , 3]
list.sort()#[0 , 1 , 2 , 3]
print(list)

#list.sort(reverse =  True) -> sorts in descending order [3 , 2 , 1] 
list.sort(reverse=True)#[3 , 2 , 1 , 0]
print(list)

#list.reverse () -> reverse the list 
list.reverse()#[0 , 1 , 2 , 3]
print(list)

#list.insert(idx,element) -> add the index and the element
list.insert(0,4)
print(list) #[4 , 0 , 1 , 2 , 3]

#list.remove(element) -> removes the element
list.remove(4)
print(list)#[0 , 1 , 2 , 3]

#list.pop(idx) -removes the index
list.pop(2)
print(list)#[0 , 1 , 2 , 3]
