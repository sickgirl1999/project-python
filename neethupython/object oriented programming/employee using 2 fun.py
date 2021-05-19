class Employee:
    company="luminar technolab"
    def setval(self,name,id,designation,salary):
        self.name=name
        self.id=id
        self.designation=designation
        self.salary=salary

    def printval(self):
        print(self.name,"\n",self.id,"\n",self.designation,"\n",self.salary,"\n")
        print(Employee.company)
emp=Employee()
emp.setval("jijo",101,"HR",20000)
emp.printval()

#2 types of variables
#static variable=related to class....call by class name
#instance variable=related to methods....call by self