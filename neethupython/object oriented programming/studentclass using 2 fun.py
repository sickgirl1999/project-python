class Student:
    def setval(self,name,std,rollno):
        self.name=name
        self.std=std
        self.rollno=rollno
    def printval(self):
        print(self.name,"\n",self.std,"\n",self.rollno)
s=Student()
s.setval("jijo","+1",28)
s.printval()