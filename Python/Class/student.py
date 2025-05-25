class student:
    def __init__(self,name,rlno,marks):
        self.name=name
        self.rlno=rlno
        self.marks=marks
    def display(self):
        print(f"name:{self.name} rlno:{self.name} marks:{self.marks}")
name = input("Enter the student's name: ")
roll_no = input("Enter the roll number: ")
marks = float(input("Enter the marks: "))

s=student(name,roll_no,marks)
s.display()
