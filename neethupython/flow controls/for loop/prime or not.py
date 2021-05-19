num=int(input("enter a number"))
flag=0
for i in range(2,num):
       if(num%i==0):
           flag=1
       else:
           flag=0
if(flag>0):
    print("not prime")
else:
    print("prime")

