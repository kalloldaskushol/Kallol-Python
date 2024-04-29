#Sets
#Sets is the collection of unique unordered items
#each elements in the set must be unique and immutable
#list & dictionary are mutable only
set1={1,2,3,4, "kallol", "Das"}
set2={1,1,2,2,3,3,4,4}
#repeated elements counted only once,so is resolved to {1,2,3,4}

null_set={} #Empty set syntex

print(set1)
print(set2)
print(type(set2))
print(len(set2))#in lenth function the duplicate valeues will get ignored

collection = set() #Empty set syntex
print(type(collection))
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.remove(3)
print(collection)

#Set Mathods
#set.add(element) -> adds an element
#set.remove(element) -> removes the given element
#set.clear() -> empties the set
#set.pop() -> removes a rendom value

#set.union(set2) -> combines both set values & returns new
#set.intersection(set2) -> combines common values $ returns new

setA={1,2,3}
setB={3,4,5}
print(setA.union(setB))
print(setA.intersection(setB))