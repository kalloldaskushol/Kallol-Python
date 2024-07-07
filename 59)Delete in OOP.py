# Delete in OOP
# del keyword is used to delete object property or the whole object itself
"""
SYNTEX ->
del s1.name = to delete the name of the object
del s1 = to delete whole object
"""

class Student():
    def __init__(self ,name):
        self.name=name
        return print(self.name)

s1 = Student("Kallol")
s1.name
del s1.name#the will be deleted
s1.name