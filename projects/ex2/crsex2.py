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
