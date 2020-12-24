class A (object):
    def dothis (self) :
        print ("A")



class B(A) :
    pass

class C(object) :
    def dothis (self) :
        print ("C")


class D (C,B) :
    pass

class G (B,C) :
    pass

x= D()
y=G()
x.dothis()
y.dothis()
