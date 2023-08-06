class Acount:
    # Constructor, Fields
    def __init__(self, Balance: float = 1000, Id: str = "***", Af_Balance: float = 0):
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
            print("Error!")
        else:
            self.Balance = value
    def Get_Id(self):
        return self.Id
    
    def Set_Id(self, value: str):
        self.Id = value
    def Update_Balance(self):
        Update_Balance = float(input("Enter update balance: "))
        self.Balance = self.Balance + Update_Balance
        return f"Your id: {self.Id} \nYour balance: {self.Balance}"
value_Balance = float(input("Enter balance: "))
value_Id = str(input("Enter Id: "))
Your_AC = Acount()
Your_AC.Set_Balance(value_Balance)
Your_AC.Set_Id(value_Id)
print(f"Your Id: {Your_AC.Get_Id()}")
print(f"Your balance: {Your_AC.Get_Balance()}")
print(Your_AC.Update_Balance())