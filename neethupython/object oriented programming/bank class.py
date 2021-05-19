class Bank:
    minbal=500
    bankname="SBI"
    def accntcreation(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

        print(self.name,"\n",self.age,"\n",self.gender,"\n",Bank.bankname)

    def deposit(self,amount):
        self.amount=amount
        bal=amount+Bank.minbal
        print("your SBI account has been credited with",self.amount)
        print("your current balance is: ",bal)
    def withdraw(self,amnt,bal):
        self.amnt=amnt
        b=bal-self.amnt
        if(self.amnt>Bank.minbal):
            print("insufficient balance")
        else:
            print("your SBI account has been debited with",self.amnt)
            print("your current balanceis",b)
b=Bank()
b.accntcreation("neethu",21,"female")
amount=int(input("enter amount to be deposited"))
bal=amount+Bank.minbal
b.deposit(amount)
amnt=int(input("enter your amount to be withdrawed"))
b.withdraw(amnt,bal)
