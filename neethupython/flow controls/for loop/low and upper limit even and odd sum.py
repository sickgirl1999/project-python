low=int(input("enterlow limit"))
upper=int(input("enter upper limit"))
oddsum=0
evensum=0

for i in range(low,upper+1):
   if (i%2==0):
        evensum=evensum+i


   else:
       oddsum=oddsum+i
print(evensum)
print(oddsum)
