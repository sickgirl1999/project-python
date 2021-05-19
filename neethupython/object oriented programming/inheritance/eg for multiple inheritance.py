class Person:
    def m1(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name, "\n", self.age, "\n", self.gender)
class Employee(Person):
    def m2(self,company,salary):
        self.company=company
        self.salary=salary
        print(self.company,"\n",self.salary)
class Student(Employee,Person):
    def m3(self,rollno):
        self.rollno=rollno
        print(self.rollno)
s=Student()
s.m3(28)
s.m2("luminar",30000)
s.m1("neethu",21,"female")