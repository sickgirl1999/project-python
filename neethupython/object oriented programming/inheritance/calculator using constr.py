class Calc:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        print(self.num1+self.num2)
    def sub(self):

        print(num1-num2)
    def mul(self):
        print(num1*num2)
    def div(self):

        print(num1/num2)

num1=int(input("enter number1"))
num2=int(input("enter number2"))
c=Calc(num1,num2)
c.add()
c.sub()
c.mul()
c.div()