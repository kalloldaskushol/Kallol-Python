#Distionary_Methods

info={
    "name" : "Kallol Das Kushol",
    "age" : 21,
    "sub" : "CSE",
    "university" : "LU"
}
#dis_name.keys() -> returns all keys
print(info.keys())

#dis_name.values() -> returns all the values
print(info.values())

#dis_name.items() -> returns all (key , value) pairs as tuples
print(info.items())

"""
Output a single tuple from the distionary 
"""
pairs = list(info.items())
print(pairs[2])

#dis_name.get("key") ->returns the key according to the value
print(info.get("name"))
print(info["name"])

"""
These two will give same output but the difference is
if we wright
print(info["name12"])
means a key that is not in the distionary then it will reply an error
but on the other hand if we use get method
print(info.get("name12"))
in that case it will not give an error it will reply a (none)
and the program will be continued
"""

#dis_name.update( {key : value} )
info.update({"city":"Sylhet" , "Country" : "BD"}) #if their are multiple items then it will be separated by a comma in the previous courly besis
print(info)