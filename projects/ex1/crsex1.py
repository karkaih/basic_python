


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
