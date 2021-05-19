maths=int(input("enter marks maths"))
eng=int(input("enter marks maths"))
mala=int(input("enter marks mala"))
soc=int(input("enter marks soc"))
total=maths+eng+mala+soc
print(total)
if total>=180:
    print("A+")
elif 160<=total<=179:
    print("A+")
elif 140<=total<=159:
    print("B+")
elif 120<=total<=139:
    print("B")
elif 100<=total<=119:
    print("C+")
elif 80<=total<=99:
    print("C")
elif 60<=total<=79:    #60<=80<=79
    print("D+")
else:
    print("fail")

