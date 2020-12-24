import os

# W
file = open ("text2.txt","w")#creat new if not exict

file.write("my name is achraf karkaih")
file.close()

file = open ("text2.txt","r")

word = file.read(30)
print(word)



# R

""" katkteb we9tma 3yeti liha  """
file = open ("text3.txt","a")#creat new if not exict
file.write("my name is achraf karkaih")
file.close()
