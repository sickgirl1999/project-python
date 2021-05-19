class Person:
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name,"\n",self.age,"\n",self.gender)
p=Person()
p.setval("jijo",23,"male")
p.printval()