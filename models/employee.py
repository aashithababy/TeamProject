class Employee:
    def __init__(self,employeename,age):
        self.employeename=employeename
        self.age=age

    def display(self):
        print(f"The employee name is {self.employeename}")