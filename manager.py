from student import Student
from dropout_student import DropoutStudent

class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self):

        roll = input("Enter Roll No : ")
        name = input("Enter Name : ")
        course = input("Enter Course : ")

        obj = Student(roll, name, course)

        self.students.append(obj)

        print("Student Added Successfully")

    def view_students(self):

        if len(self.students) == 0:
            print("No Student Found")
            return

        for student in self.students:
            student.display()

    def search_student(self):

        roll = input("Enter Roll No : ")

        for student in self.students:

            if student.roll_no == roll:
                student.display()
                return student

        print("Student Not Found")
        return None

    def mark_dropout(self):

        roll = input("Enter Roll No : ")

        for i in range(len(self.students)):

            if self.students[i].roll_no == roll:

                reason = input("Enter Dropout Reason : ")

                student = self.students[i]

                obj = DropoutStudent(
                    student.roll_no,
                    student.name,
                    student.course,
                    reason
                )

                self.students[i] = obj

                print("Student Marked as Dropout")
                return

        print("Student Not Found")

    def delete_student(self):

        roll = input("Enter Roll No : ")

        for student in self.students:

            if student.roll_no == roll:
                self.students.remove(student)
                print("Student Deleted")
                return

        print("Student Not Found")