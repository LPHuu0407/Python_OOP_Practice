import math
class Circle:
    # Fields, Constructor
    def __init__(self, value_r : float = 1):
        #Validations
        #Assign to self object
        self.r = value_r
    #Properties, Methods
    def Get_r(self):
        return self.r
    def Set_r(self, Value):
        if Value <= 0:
            print("Value of radius not is 0!")
            self.r = 1
        else:
            self.r = Value
    def Input_r(self):
        self.r = float(input("Enter the radius of the circle: "))
        self.Set_r(self.r)
    def Output_r(self):
        return f" - Radius of the circle: {self.Get_r()}"
    def Area_of_Circle(self):
        return f" - Area of the circle: {math.pi * self.Get_r() ** 2}"
    def Perimeter_of_Circle(self):
        return f" - Perimeter of the circle: {2 * math.pi * self.Get_r()}"
Circle_Object = Circle()
Circle_Object.Input_r()
print(Circle_Object.Output_r())
print(Circle_Object.Area_of_Circle())
print(Circle_Object.Perimeter_of_Circle())