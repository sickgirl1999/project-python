class Person:
    def set(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name,"\n",self.age,"\n",self.gender)
class Employee(Person):
    def det(self,company,salary):
        self.company=company
        self.salary=salary
        print(self.company,"\n",self.salary)
p=Person()
p.set("jijo",23,"male")
e=Employee()
e.det("luminar",30000)
e.set("neethu",21,"female")