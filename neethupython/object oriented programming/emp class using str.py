class Employee:
    def __init__(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
        print(self.name,"\n",self.age,"\n",self.id,"\n",self.salary)
    def __str__(self):
        return str(self.id)+self.name
e=Employee("jijo",21,101,20000)
print(e)