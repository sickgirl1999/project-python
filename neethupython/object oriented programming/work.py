class Work:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def __str__(self):
        return self.name
lst=[]
f=open("work","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=data[3]
    obj=Work(name,rollno,course,mark)
    lst.append(obj)
for i in lst:
    if i.mark>190:
        print(i)