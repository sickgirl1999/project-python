class Vehicle:
    def features(self,type,color,brand):
        self.type=type
        self.color=color
        self.brand=brand
        print(self.type,"\n",self.color,"\n",self.brand)
v=Vehicle()
v.features("car","red","toyota")