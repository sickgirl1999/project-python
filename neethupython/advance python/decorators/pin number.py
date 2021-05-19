#custom exception
#raise Exceeption
# age=int(input("enter your age"))
# if age>=18:
#     print("eligible for vaccination")
# else:
#    raise  Exception("you are not eligible for vaccination")
def admin_req(func):
    def wrapper(user,pin):
        if user!="admin":
            raise  Exception("you are not allowed")
        else:
            return func(user,pin)
    return wrapper

def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_req
def delete_account(user,accno):
    return str(accno)+"deleted"
print(change_pin("user",1000))
print(delete_account("admin",1000))

