class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,"\n",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def prints(self):
        print(self.rollno,"\n",self.mark)
s=Student(28,34,"neethu",21)
s.prints()
s.print()