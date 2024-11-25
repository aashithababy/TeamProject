class admin:
    def __init__(self,adminname,age):
        self.adminname=adminname
        self.age=age

    def display(self):
        print(f"The admin name is {self.adminname}")