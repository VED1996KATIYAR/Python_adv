def student(sid,name,*marks):
    if len(marks)==0:
        print(f"The name is {name}  and the id is {sid} and he is absent in all exams")
    else:
        percent=sum(marks)/len(marks)
        print(f"The name is {name}  and the id is {sid} and he got {percent}%")
        print(marks)

student(101,"John",87.0,95.0,69.5,81.5,74.0)


def student1(sid,name,**marks):
    if len(marks)==0:
        print(f"The name is {name}  and the id is {sid} and he is absent in all exams")
    else:
        percent=sum(marks.values())/len(marks)
        print(f"The name is {name}  and the id is {sid} and he got {percent}%")
        print(marks)

student1(101,"John",PHY=87.0,CHEMISTRY=95,MATHS=69.5,BIOLOGY=81.5,PED=74.0)
