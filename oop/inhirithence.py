class calcul :
    def __init__(self,a,b):
        self.a =a
        self.b=b


    def add(self) :
        print(self.a + self.b)

    def mul(self) :
        print(self.a * self.b)


class sccalcul (calcul) :
    def power(self) :
        print(pow(self.a,self.b))
 


x = sccalcul(2,3)

x.add()
x.mul()
x.power()
