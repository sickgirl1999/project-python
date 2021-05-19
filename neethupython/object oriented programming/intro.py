# class=design pattern
# object=real world entity
# reference=name that refers a memory loc of a object  #f=open(F)file reference
class Person:
    def print(self,name,age,gender):  #self=instance variable
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name,"\n",self.age,"\n",self.gender)
p=Person()
p.print("jijo",23,"male")
e=Person()
e.print("neethu",21,"female")

