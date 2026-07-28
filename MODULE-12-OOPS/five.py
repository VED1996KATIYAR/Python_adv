class Student:
    college_name="ABC College"
    department=["arts","commerce","science"]

    def __init__(self,name,rollno):
        print("Calling the situation")
        self.name=name
        self.rollno=rollno
        print(f"The name of the students is {self.name} and the roll no is {self.rollno}")

    @classmethod
    def greet1(self):
        print(f"Hello welcome to the {self.college_name}")
        for i in self.department:
            print(i)

    @staticmethod
    def greet():{
        print("Hello")
    }

    def study(self,hours):
        print(f"The student daily study for {hours} hour")

Student1=Student("Ved Katiyar",1000)
Student1.greet1()
Student1.greet()
Student1.study(8)
print(Student1.college_name,Student1.department)

