class student :
    def __init__ (self , name) :
         self.name = name
         self.marks=[]
         print("welcome {} in the school".format(self.name) )


    def add_marks(self,mark ) :
        self.marks.append(mark)


    def avge(self) :
        return (sum(self.marks)/len(self.marks))



s1 = student("achraf" )
s1.add_marks(10)
s1.add_marks(20)
s1.add_marks(18)
print(s1.marks)
print(s1.avge())
