age=int(input("enter your age"))
sex=input("enter your sex 1.F 2.M")
status=input("enter your status 1.S 2.M")
if sex=="F":
    print("you can work only in urban areas")
elif (sex=="M" and 20<=age<=40):
      print("you can work anywhere")
elif(sex=="M" and 40<=age<=60):
    print("you can work only in urban areas")
else:
  print("ERROR")

