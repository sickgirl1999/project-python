employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"devoloper"},
    1001:{"eid":1001,"name":"arun","salary":26000,"designation":"devoloper"},
    1002:{"eid":1002,"name":"ajay","salary":27000,"designation":"hr"},
    1003:{"eid":1003,"name":"vinay","salary":28000,"designation":"devoloper"},
    1004:{"eid":1004,"name":"kiran","salary":29000,"designation":"devoloper"},

}
# eid=int(input("enter user  id"))  #1000
# prop=input("enter property options=[eid,name,salary,designation]") #salary
# if (eid in employees)&(prop in employees[eid]):
#     print(employees[eid][prop])
# else:
#     print("enter valid eid")



def print_employees(**kwargs):
    id=kwargs["id"]
    prop=["name,salary,designation"]
    # designation=kwargs["designation"]
    if id in employees:
        print(employees[id])
    else:
        print("invalid id")
print_employees(id=1003)
#eid and desig
