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
