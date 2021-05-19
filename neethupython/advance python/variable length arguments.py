#args *args
# def add(num1,num2):  #parametres
#     return num1+num2
# sum=add(10,20)  #Arguments
# print(sum)
#add 3 numbers
#addThree()  first camlin notation
#add_three() snake notation
# def add_three(num1,num2,num3):
#     return num1+num2+num3
# res=add_three(10,10,10)
# print(res)

# def add(*args):  #args is tuple,it takes any no of args
#     print(args)
# add(10)
# add(10,10)
# add(10,10,10)

# def add(*args):  #10,20
#     res=0
#     for i in args: #10 20
#         res+=i #0+10=10+20=30
#     return res

# print(add(10,20))

# def print_employee(**kwargs):
#     for k,v in kwargs.items():
#
#         print(k,":",v)
#
# print_employee(id=100,place="ekm",name="neethu")

# arr=[10,2,7,4,8]
# # arr.sort(reverse=True) #method
# s=sorted(arr,reverse=True) #sorted=fun
# print(s)
#  #diff b/w *args and **kwargs
# args=tuple
# kwargs=dict

# def print_employee(**kwargs):  type of args is dic so we can add values as key value pair
#     print(kwargs)
# print_employee(id=101,name="neethu",sal=10000)
employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"devoloper"},
    1001:{"eid":1001,"name":"arun","salary":26000,"designation":"devoloper"},
    1002:{"eid":1002,"name":"ajay","salary":27000,"designation":"hr"},
    1003:{"eid":1003,"name":"vinay","salary":28000,"designation":"devoloper"},
    1004:{"eid":1004,"name":"kiran","salary":29000,"designation":"devoloper"},

}
def print_employees(**kwargs):
    id=kwargs["id"]
    if id in employees:
        print(employees[id]["name"])
    else:
        print("invalid id")
print_employees(id=1003)
