print ("This Game Will Take Several Numbers And Print The Average ")


ct = 0
x= []
number = int (input  ("How many nUmber would You like to sum"))

for i in range (number) :
    stt ='Enter the {} st  : '.format(i+1)
    
    nm = float (input(stt ))
    print(i)
    x.insert(i ,nm)
    ct = x[i]+ct


for s in range(len(x)) :
    print (x[s] ,"\t" , end ="")

print()   
print("result summ is :" ,ct)
print("result avg is :" , ct/number)

    
