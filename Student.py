class Student:
    #Fields, Constructor
    def __init__(self, Value_ID: str = "", Value_Name: str = "", Value_Year: int = 1900, Value_Location: str = ""):
        #Validations
        #Assign to self object
        self.StudentID = Value_ID
        self.Full_Name = Value_Name
        self.Year_of_Birth = Value_Year
        self.Location = Value_Location
    #Properties, Methods
    # <Get, set of StudentID>
    def Get_StudentID(self):
        return self.StudentID
    def Set_StudentID(self, value: str):
        self.StudentID = value
    # <Get, set of Full_Name>
    def Get_Full_Name(self):
        return self.Full_Name
    def Set_Full_Name(self, value: str):
        self.Full_Name = value
    # <Get, set of Year_of_Birth>
    def Get_Year_of_Birth(self):
        return self.Year_of_Birth
    def Set_Year_of_Birth(self, value: int):
        self.Year_of_Birth = value
    # <Get, set of Location>
    def Get_Location(self):
        return self.Location
    def Set_Location(self, value: str):
        self.Location = value
    def Input_Information(self):
        Value_ID = str(input("Enter your ID: "))
        Value_Name = str(input("Enter your full name: "))
        Value_Year = int(input("Enter your year of birth: "))
        Value_Location = str(input("Enter your location: "))
        self.Set_StudentID(Value_ID)
        self.Set_Full_Name(Value_Name)
        self.Set_Year_of_Birth(Value_Year)
        self.Set_Location(Value_Location)
    def Ouput_Information(self):
        Age = 2023 - self.Get_Year_of_Birth()
        return f"- Your ID: {self.Get_StudentID()} \n- Your full name: {self.Get_Full_Name()} \n- Your year of birth: {self.Get_Year_of_Birth()} \n- Your location: {self.Get_Location()} \n- Your age: {Age}"
Instance_Student_1 = Student()
Instance_Student_1.Input_Information()
print(Instance_Student_1.Ouput_Information())