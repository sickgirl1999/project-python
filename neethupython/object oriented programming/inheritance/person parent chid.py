class Person:
    def m1(self,name,age):
        self.name=name
        self.age=age
        print(self.name,"\n",self.age)
class Child(Person):
    def m2(self,rollno):
        self.rollno=rollno
        print(self.rollno)
class Parent(Person):
    def m3(self,job):
        self.job=job
        print(self.job)
class Student(Child):
    def m4(self,std):
        self.std=std
        print(self.std)
s=Student()
s.m4("+2")
s.m2(28)
s.m1("neethu",23)
p=Parent()
p.m3("accountant")