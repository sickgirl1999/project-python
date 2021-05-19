curyear=int(input("enter current year"))
curmonth=int(input("enter current month"))
curday=int(input("enter current date"))
byear=int(input("enter your birth year"))
bmonth=int(input("enter your birth month"))
bday=int(input("enter your birth date"))
if (curday==bday)&(curmonth==bmonth):
    age=curyear-byear
    print(age)


