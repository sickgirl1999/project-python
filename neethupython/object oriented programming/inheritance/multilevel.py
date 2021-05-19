class Parent:
    def m1(self):
        print("inside parent")
class Child(Parent):
    def m2(self):
        print("inside child ")
class Subchild(Child):
    def m3(self):
        print("inside subchild")
obj=Subchild()
obj.m3()
obj.m2()
obj.m1()
obj2=Child()
obj2.m2()
obj2.m1()