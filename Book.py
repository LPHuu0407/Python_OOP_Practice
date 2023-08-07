class Book:
    #Constructor, Fields
    def __init__(self, bookID: str = "" , nameBook: str = "", priceBook: float = 0, saleBook: float = 0):
        # Validations
        assert priceBook >= 0, f"Error of <priceBook> !"
        assert saleBook >= 0, f"Error of <saleBook> !"
        # Assign to self object
        self.BookID = bookID
        self.NameBook = nameBook
        self.PriceBook = priceBook
        self.SaleBook = saleBook
    #Properties, Methods
    def Get_BookID(self):
        return self.BookID
    def Set_BookID(self, value):
        if type(value) is str and len(value) != 0:
            self.BookID = value
        else:
            print("ID of the book isn't number or empty!")
    def Get_NameBook(self):
        return self.NameBook
    def Set_NameBook(self, value):
        if type(value) is str and len(value) != 0:
            self.NameBook = value
        else:
            print("Name of the book isn't number or empty!")
    def Get_PriceBook(self):
        return self.PriceBook
    def Set_PriceBook(self, value):
        if type(value) is float and value >= 0:
            self.PriceBook = value
        else:
            print("Price of the book isn't less than 0!")
    def Get_SaleBook(self):
        return self.SaleBook
    def Set_SaleBook(self, value):
        if type(value) is float and value > 0:
            self.SaleBook = value
        else:
            print("Sale of the book isn't less than 0!")
    def Input_Information(self):
        value_BookID = str(input(f"Enter BookID: "))
        value_NameBook = str(input(f"Enter NameBook: "))
        value_PriceBook = float(input(f"Enter PriceBook: "))
        value_SaleBook = float(input(f"Enter SaleBook: "))
        self.Set_BookID(value_BookID)
        self.Set_NameBook(value_NameBook)
        self.Set_PriceBook(value_PriceBook)
        self.Set_SaleBook(value_SaleBook)
    def Output_Information(self):
        sale = self.Get_PriceBook() - self.Get_SaleBook()
        return f" - ID of the book: {self.Get_BookID()} \n - Name of the book: {self.Get_NameBook()} \n - Price of the book: {self.Get_PriceBook()}VND \n -Sale of the book: {self.Get_SaleBook()}VND \n -Total: {sale}VND"
    def Update_Information(self):
        self.Input_Information()
print("Information current:")
Book_Item = Book()
Book_Item.Input_Information()
print(Book_Item.Output_Information())
Book_Item.Update_Information()
print("Information after update:")
print(Book_Item.Output_Information())