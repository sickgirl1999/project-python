class Addition:
    def setval(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printval(self):
        print(self.num1+self.num2)
a=Addition()
num1=int(input("enter num1"))
num2=int(input("enter num2"))
a.setval(num1,num2)
a.printval()