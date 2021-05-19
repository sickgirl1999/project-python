#map......op=ip
#filter
#reduce()

# lst=[2,3,4,5,6]
# #op squares of all obj
# sq=[]
# for i in lst:
#     res=i**2
#     sq.append(res)
# print(sq)
lst=[2,3,4,5,6,7]
#squares
def squares(num):
    return num**2
squares=list(map(squares,lst))  #frst arg should be fun and second one is iterable
print(squares)

#lambda
squares=list(map(lambda num:num**2,lst))  #frst arg should be fun and second one is iterable
print(squares)

employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"devoloper"},
    1001:{"eid":1001,"name":"arun","salary":26000,"designation":"devoloper"},
    1002:{"eid":1002,"name":"ajay","salary":27000,"designation":"hr"},
    1003:{"eid":1003,"name":"vinay","salary":28000,"designation":"devoloper"},
    1004:{"eid":1004,"name":"kiran","salary":29000,"designation":"devoloper"},

}






