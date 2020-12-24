## even = / 2
## odd != /2

number = input ("Enter A Number : ")

while number != 'x' :
   
    try :
        number = int(number)
    
        if number%2 == 0 :
        
            print ("even")


        else :
        
            print("odd")
            
          
    except ValueError :
        print('Please Enter A Valid Number')
        
    number = input ("Enter A Number : ")
     
print ("close")
