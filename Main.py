import Account, Book, Cars, Circle, Student
# Account
Acount_Object = Account()
Acount_Object.Input_Balance_Id()
print(Acount_Object.Output_Balance_Id())
print(Acount_Object.Update_Balance())
# Book
print("Information current:")
Book_Item = Book()
Book_Item.Input_Information()
print(Book_Item.Output_Information())
Book_Item.Update_Information()
print("Information after update:")
print(Book_Item.Output_Information())
# Cars
# Circle
Circle_Object = Circle()
Circle_Object.Input_r()
print(Circle_Object.Output_r())
print(Circle_Object.Area_of_Circle())
print(Circle_Object.Perimeter_of_Circle())
# Student
Instance_Student_1 = Student()
Instance_Student_1.Input_Information()
print(Instance_Student_1.Ouput_Information())