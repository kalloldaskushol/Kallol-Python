#Distionary
#Distionaries are used to store data values in 
# key : value
#pairs

#They are unordered,mutable(CHANGEABLE) & don't aallow duplicate keys
"""
distionary_name = {
    key : value ,
    key2 : value2
}
"""
#We can't use same key twice,,if we write twice then the previous one will be modifed
info = {
    "key" : "value" ,
    "name" : "Kallol"  ,
    "age" : 21 ,
    "is adult" : True ,#Bulion can be added
    12 : 13 , #keys can be also a number,distionary
    "studies" : "CSE" ,
    "cgpa" : 5.00 ,#Float can be added
    "subjects" : ["python" , "C" , 'java'], #List can be added
    "topics" : ("distionary" , "Sets") ,
}
print(type(info))
print(info["key"])
print(info["name"])
print(info["subjects"])
print(info["cgpa"])
print(info[12])
print(info["topics"])

info["name"] = "Kushol" #We can change the value
info["surname"] = "Das"
print(info["name"])
print(info["surname"])
print(info)

#Nested Distionary

student = {
    "name" : "Kallol Das Kushol" , 
    "marks" : {
        "chem" : 98,
        "phy" : 99,
        "math": 99.6,
    }
}
print(student["marks"]["chem"])
print(student["marks"]["phy"])
print(student["marks"] ["math"])
print(student["marks"])