low=int(input("enterlow limit"))
upper=int(input("enter upper limit"))
for i in range(low,upper+1):
    if(i%2==0):
        print(i)