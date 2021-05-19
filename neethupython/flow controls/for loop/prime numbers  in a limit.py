limit=int(input("enter a limit"))
flag=0
for i in range(1,limit):
    for j in range(1,limit):
        if(limit%i==0):
            flag=1
        else:
            flag=0
    if(flag>0):
        print("not prime")
    else:
        print("prime")

