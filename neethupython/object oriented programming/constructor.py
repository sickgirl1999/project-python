#con=to initialize instance variable
#automatically invoke when creating object
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name,"\n",self.age,"\n",self.gender)
p=Person("jijo",23,"male")
p.printval()