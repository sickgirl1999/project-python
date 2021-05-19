names=["ajay","aravind"]
upp=list(map(lambda name:name.upper(),names))
print(upp)


#terinary operator
num1=10
num2=20
larg=num1 if num1>num2 else num2
print(larg)

lst=[7,8,9,4,3,2]
op=[]
for num in lst:
    op.append((num+1)) if num>5 else op.append((num-1))
print(op)

lst=[7,8,9,4,3,2]
op=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(op)



