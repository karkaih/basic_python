
#read 

import os
"""b for binary"""
file = open ("text1.txt",'r' )

print("Name of file  :" ,file.name)


print("Closer or Not :" ,file.closed)


print("Opening Mode   :" ,file.mode)

"""

words = file.read()

print(words)

print("2 way ")

"""

print(file.tell())

re = file.readlines()

print(re)


print(file.tell())

