# # Beak statment]
# import time
# for i in "DevOps":
#     print(i)
#     if i == "O":
#         print ("I have found what I was looking for ")
#         continue
#     time.sleep(1)

    
# print("Out of the Loop")
import openai
import os
import random
import time
Names = ["Joe","John","Jessica"]
random.shuffle(Names)
print("Throwing a Dice of contestant" , Names)

print("Lets see who is Lucky")
print ("lOADING.......25%")
time.sleep(1)
print ("lOADING.......50%")
time.sleep(1)
print ("lOADING.......70%")
time.sleep(2)
print ("lOADING.......100%")

LUCKY=random.choice(Names)
print(LUCKY, "Is a winner")