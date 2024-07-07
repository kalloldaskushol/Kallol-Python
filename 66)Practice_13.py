#Pracrice

#Define a circle class to create a circle with radius r using the constructor
#define an area() method of the class which calculates the area of the circle.
#define a perimeter() method of the class which allows to calculate the perimeter of the circle.

class Circle():
    def __init__(self,redius):
        self.redius = redius
    
    def area(self):
        return print(3.1416 * self.redius ** 2)
    
    def perimeter(self):
        return print(2* 3.1416 * self.redius)

c1 = Circle(5)
c1.area()
c1.perimeter()

print("END>>>>>>")

# Define a Employee class with attributes role,,department & salary. Also include a showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes : name & age


class Employee():
    def __init__(self,role,dep,sal):
        self.role = role
        self.dep = dep
        self.sal = sal

    def show_details(self):
        print("Role =", self.role)
        print("Department =",self.dep)
        print("Salary =",self.sal,"/- TK")

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Engineer_name =",self.name)
        print("Age =",self.age)

        super().__init__("Chief","CE",500000)

e1 = Employee("CEO","XYZ",100000)
e1.show_details()

e2 =Engineer("Kallol",15)
e2.show_details()
print("END<<<<<<<")
#Create a class called Order which stores item & price.
# Use Dunder function _ _ gt _ _ () to convey that:
    # order1 > order2 -> if price of order1 > price of order2

class Order():
    def __init__(self,item,price):
        self.item =item
        self.price  = price
    def __gt__(self,order2):
        return print(self.price > order2.price)
    
order1 = Order("Chips",15)
order2 = Order("Tea",20)

order1 > order2 # type: ignore
order2 > order1 # type: ignore