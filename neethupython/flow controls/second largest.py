#nested if
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd bumber"))
if (num1>num2)&(num1>num3):
    if num2>num3:
       print(num2,"second largest")
    else:
       print(num3, "second largest")
elif (num2>num1)&(num2>num3):
    if num1>num3:
        print(num1,"Second largest")
    else:
         print(num3, "second largest")

elif (num3>num1)&(num3>num2):
    if num1>num2:
        print(num1,"second largest")
    else:
        print(num2,"second largest")