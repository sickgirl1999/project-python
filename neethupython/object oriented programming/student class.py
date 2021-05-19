
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,"\n",self.age)
    def __str__(self):
        return self.name
f=open("student","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    name=data[0]
    age=data[1]
    obj=Student(name,age)
    print(obj)
