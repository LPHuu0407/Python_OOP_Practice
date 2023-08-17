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
                print(f" - Radius recent input: {self.Circle_Array[i]}")
        else:
            print("Number of the circle isn't less than 0!")
    def Output_r(self):
        print(f"{self.number_of_Circle} radius entered:")
        for i in range(0, self.number_of_Circle):
            print(f" - Radius: {self.Circle_Array[i]}")
Cir = Circle()
Cir.Input_r()
Cir.Output_r()