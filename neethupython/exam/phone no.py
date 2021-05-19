import re
f=open("phoneno","r")
x="[+][9][1][0-9]{10}"
p=open("phno","w")
q=open("phno","a")
for i in f:
    i=i.rstrip("\n")
    match=re.fullmatch(x,i)
    if match is not None:
        q.write(i)
        q.write("\n")
    else:
        print(i,"is invalid")