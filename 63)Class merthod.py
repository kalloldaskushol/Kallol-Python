#Class merthod

# A class method is bound to the class & receives the class as an implicit first argument

# Note - static method can't access or modify class state & generallu for utility

"""
there are basically 3 types of methods
1.static methods -> no argument
2.instance methods -> to modify instance data
3.class methods -> to modify the class attributes"""

class Person():
    name = "Annonymous"

    def ChangeName (self,name):
        self.name = name
        # Person.name = name

p1 = Person()
p1.ChangeName("kallol Das Kushol")

print(p1.name)
print(Person.name)

#As we can see it is only changing name in the method but the name veriable on the class is still anonymous
# If we want to Change the name attribute in the class we can use the class mathod or we can put (Person) instead of (self)

class Cls_method_Learn ():
    cls_name = "Unknown"

    @classmethod
    def cng_name(cls,name):
        cls.name = name

p2 = Cls_method_Learn()
p2.cng_name("Kallol")

print(p2.name)
print(Cls_method_Learn.name)

# by using the class method we can change the class attributes

