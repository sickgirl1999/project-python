#single inheritance
class Person:  #parentclass,baseclass,superclass
    def set(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print(self):
        print(self.name,"\n",self.age,"\n",self.gender)
class Student(Person):  #derivedclass,childclass,subclass
    def det(self,rollno):
        self.rollno=rollno
    def prints(self):
        print(self.rollno)
p=Person()
p.set("neethu",21,"female")
p.print()
s=Student()
s.det(28)
s.prints()
s.set("jijo",23,"male")
s.print()