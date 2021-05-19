sal=int(input("enter your salary"))
ser=int(input("enter your experience"))
bonus=sal+sal*5/100
if(ser>5):
    print("you are eligible for bonus")
else:
    print("you are not eligible for bonus")
print("your salary+bonus is:",bonus)
