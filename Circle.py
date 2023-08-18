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
        self.number_of_Circle = int(input("Enter number of the circle: "))
        self.Circle_Array = Arr.array('f', [])
        if self.number_of_Circle >= 1:
            for i in range(0, self.number_of_Circle):
                self.Set_r(float(input(f"Enter value of radius {i + 1}: ")))
                self.Circle_Array.append(self.Get_r())
                print(f" - Radius recent input: {self.Circle_Array[i]} cm")
        else:
            print("Number of the circle isn't less than 0!")
    def Output_r(self):
        print(f"{self.number_of_Circle} radius entered:")
        for i in range(0, self.number_of_Circle):
            print(f" - Radius: {self.Circle_Array[i]} cm")
    def Area(self):
        self.Array_Area = Arr.array('f', [])
        print(f"Area of {self.number_of_Circle} circles:")
        for i in range(0, self.number_of_Circle):
            self.Area_Circle = math.pi * self.Circle_Array[i] ** 2
            self.Array_Area.append(self.Area_Circle)
            print(f" - Area circle {i + 1}: {self.Area_Circle} cm2")
Cir = Circle()
Cir.Input_r()
Cir.Output_r()
Cir.Area()