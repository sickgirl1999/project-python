class Employee:
    company="luminar technolab"
    def __init__(self,name,id,designation,salary):
        self.name=name
        self.id=id
        self.designation=designation
        self.salary=salary

    def printval(self):
        print(self.name,"\n",self.id,"\n",self.designation,"\n",self.salary,"\n")
        print(Employee.company)
emp=Employee("jijo",101,"HR",30000)
emp.printval()
