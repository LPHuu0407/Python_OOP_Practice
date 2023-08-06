class Acount:
    # Constructor, Fields
    def __init__(self, Balance: float = 1, Id: str = "***", Af_Balance: float = 0):
        # Run validations to the received argument
        assert Balance > 0, f"{Balance} is not = 0 or {Balance} is not < 0"
        assert Af_Balance >= 0, f"{Af_Balance} is not = 0 or {Af_Balance} is not < 0"
        # Assign to self object
        self.Id = Id
        self.Balance = Balance
    # Methods, getter, setter
    def Get_Balance(self):
        return self.Balance
    def Set_Balance(self, value: float):
        if value < 0:
            print("Balance can't be less than 0!")
        else:
            self.Balance = value
    def Get_Id(self):
        return self.Id
    
    def Set_Id(self, value: str):
        self.Id = value
    def Input_Balance_Id(self):
        self.Set_Balance(float(input("Enter balance: ")))
        self.Set_Id(str(input("Enter Id: ")))
    def Output_Balance_Id(self):
        return f" - Your id: {self.Get_Id()} \n - Your balance: {self.Get_Balance()}VND"
    def Update_Balance(self):
        Update_Balance = float(input("Enter update balance: "))
        self.Set_Balance(self.Get_Balance() + Update_Balance)
        return f" - Your id: {self.Get_Id()} \n - Your balance: {self.Get_Balance()}VND"
Acount_Object = Acount()
Acount_Object.Input_Balance_Id()
print(Acount_Object.Output_Balance_Id())
print(Acount_Object.Update_Balance())