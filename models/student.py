class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"The student name is {self.name}")