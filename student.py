class Student:

    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.status = "Active"

    def display(self):
        print("\n------------------------")
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Course  :", self.course)
        print("Status  :", self.status)