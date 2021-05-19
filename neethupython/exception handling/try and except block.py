# a=int(input("enter a number"))
# b=int(input("enter a number"))
# try:     #run always
#     print(a/b)
# except:
#     print("exception occured")


a=[1,2,3]
b=int(input("enter your index"))
try:
    print(a[b])
except:
    print("index out of range")
finally:  #it works all time like try
    print("finally")



