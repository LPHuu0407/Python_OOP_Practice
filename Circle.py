import math
import array as Arr
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
        number_of_Circle = int(input("Enter number of the circle: "))
        Circle_Array = Arr.array('f', [])
        if number_of_Circle >= 1:
            for i in range(0, number_of_Circle):
                self.Set_r(float(input(f"Enter value of radius {i + 1}: ")))
                Circle_Array.append(self.Get_r())
                print(f"Radius recent input {i + 1}: {Circle_Array[i]}")
        else:
            print("Number of the circle isn't less than 0!")




        
    def Output_r(self):
        return f" - Radius of the circle: {self.Get_r()}"
    def Area_of_Circle(self):
        return f" - Area of the circle: {math.pi * self.Get_r() ** 2}"
    def Perimeter_of_Circle(self):
        return f" - Perimeter of the circle: {2 * math.pi * self.Get_r()}"