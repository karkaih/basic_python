class animal :
    def __init__(self,name) :
        self.name = name
        print("name is " , self.name)


class Dog(animal) :
    def __init__(self, nom ):
        super().__init__(nom)
        self.food ="fish"
       
        print("food is " , self.food)


x= Dog("achraf")

