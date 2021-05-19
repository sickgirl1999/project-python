
name=input("enter your name")
place=input("enter your location")
age=int(input("enter your age"))
health=input("do yo have any health issues=True/False")
def decor(func):
    def wrapper(**kwargs):
        if (age>65)or(health==True):
            return func(**kwargs)
        else:
            raise Exception("you are not allowed")
    return wrapper
@decor
def vaccine_portal(**kwargs):
    print("ordered id location is ekm")
vaccine_portal()