class Game :
#+++++++++++++++++++++++++++++++++++++++++++++++++    
    def __init__(self):
        print("Welcome In The Full Game")
        print("Choose your game from our collection")
        print("Press 1 : Play Even-Odd Game")
        print("Press 2 : Play Sum-Avg Game")
        print("Press 3 : Play Multiplication Table Game")
        self.choose()
#+++++++++++++++++++++++++++++++++++++++++++++++++
    def choose(self) :
        while True :
            user_choise = input("Enter Your Choise")
            if user_choise == 'x' :
                print("Close")
                break
            try:
                user_choise =int(user_choise)
                if user_choise == 1 :
                    print("Even Odd Game")
                    self.Even_Odd_Game()
                elif  user_choise == 2 :
                    print("Sum Avg Game")
                    self.Sum_Average_Game()
                elif  user_choise == 3 :
                    print("Multiplication Table Game")
                    self.Multip_Game()
                else :
                    print("Please chose between [1-3]")
            except ValueError :
                print("Enter A valid Number")
#+++++++++++++++++++++++++++++++++++++++++++++++++
    def Even_Odd_Game(self):
        print ("Welcome In the Even-Odd Game")
        while True :
            number =  input ("Please Enter A number").lower()
            if number == 'x' :
                print("Close")
                break
            try :
                number = int(number)
                if number%2 == 0 :
                    print("even")
                else:
                    print("odd ")

            except ValueError :
                print("Enter A valid Number or 'x' to Exit")
        print("------------------------------------------")

#+++++++++++++++++++++++++++++++++++++++++++++++++

    
    def Sum_Average_Game(self) :
        print ("This Game Will Take Several Numbers And Print The Average ")
        number = int (input  ("How many nUmber would You like to sum"))
        cr_c = 0
        summ = 0
        while cr_c < number :
            nm = float (input ("Enter The Number : "))
            summ +=nm
            cr_c+=1
        print("summ all Numbers = ",summ)
        print("The Avg is : " , summ/number)

#+++++++++++++++++++++++++++++++++++++++++++++++++
    def Multip_Game (self) :
        print ("Enter the number That you want to multiple")
        number = int(input ())

        for i in range (1,13) :
            st = '{} * {} :' .format(number,i)
            print(st , number*i)
        print("+++++++++++++++++++++++ multiplication tab ++++++++++++++++++++++++++")
        start = int(input ("start"))
        end = int(input ("end"))
        for s in range (start,end+1) :
            print("___________ tab of ",s," _______________")
            for j in range (1,13):
                st = '{} * {} :' .format(s,j)
                print(st , s*j)


#+++++++++++++++++++++++++++++++++++++++++++++++++

Game1 = Game()

#Create Class
#Methode-Pass
#Copy Projects
#Create Choices Method
#Handling Exception

