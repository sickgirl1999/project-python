class Person:
    def m1(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name,"\n",self.age,"\n",self.gender)
class Employee(Person):
    def m2(self,company,salary):
        self.company=company
        self.salary=salary
        print(self.company,"\n",self.salary)
class Student(Employee):
    def m3(self,rollno):
        self.rollno=rollno
        print(self.rollno)
obj=Student()
obj.m3(28)
obj.m2("luminar",20000)
obj.m1("neethu",21,"male")
obj2=Employee()
obj2.m2("infotech",30000)
obj2.m1("anu",23,"female")
