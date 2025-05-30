class dept:
    def inp(self):
        self.n=input("enter a name of department=  ")
        self.c=input("enter college name=  ")
class std(dept):
    def inpu(self):
        self.name=input("enter a name of student=  ")
        self.rollno=int(input("enter a roll no=  "))
        print("student name is  ",self.name,"student rollno is ",self.rollno,"student college is ",self.c,"student depatment= ",self.n)
s=std()
s.inp()
s.inpu()


"""
enter a name of department=  cm
enter college name=  s.e.s.p
enter a name of student=  jiya
enter a roll no=  2501
student name is   jiya student rollno is  2501 student college is  s.e.s.p student depatment=  cm


"""