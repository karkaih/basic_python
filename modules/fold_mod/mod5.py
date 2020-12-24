import os
import time 
"""
#create dir
# os.mkdir("achraf")
"""
#current loc
print(os.getcwd())

#ghaydkhel lwest fold achraf 
os.chdir("achraf")

os.mkdir("ach")

print(os.getcwd())


#mse7 dir
time.sleep(5)
os.rmdir("ach")

print(os.getcwd())
