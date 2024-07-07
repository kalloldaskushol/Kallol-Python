# Super() Method
# Super() method is used to access methods of the parent class
# We can give value to the previous attribute/variable by using super method


class Car():
    def __init__(self,Colour):
        self.colour = Colour
        return print(Colour)
    
    @staticmethod
    def start():
        print("Car started....")
        
    @staticmethod
    def stop():
        print("car stoped....")

class ToyotaCar(Car):
    def __init__(self,Model_name,Colour):
        self.name = Model_name
        #if we use self.colour then the input colour will be changed in the child class
        #so if we want to change the colour in the base class which is located in the init function
        #in this case we use super() method

        super().__init__(Colour)
        super().start()

car1 = ToyotaCar("Fortuner","Black")
car1.colour