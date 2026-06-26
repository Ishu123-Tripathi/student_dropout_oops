from student import Student

class DropoutStudent(Student):

    def __init__(self, roll_no, name, course, reason):
        super().__init__(roll_no, name, course)
        self.reason = reason
        self.status = "Dropout"

    def display(self):
        super().display()
        print("Reason  :", self.reason)