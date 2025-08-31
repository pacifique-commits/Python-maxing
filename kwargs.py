# Variable Lengs Arguments *Kwargs (kewword Argument)
# Args are turple 
# Kwargs are dictionary
#Kurwa
import random
def time_activity(*args, **kwargs):
     
     #args represent tuple # kwargs : dictionnary
     '''
      Input: Multple value for minutes, key=value pair activity
      output : return sum of minutes + random munute spect on rndm activity
     '''
     print (args) 
     print (kwargs)
     min = sum(args)+random.randint(0, 60)
     print(min)
     choice = random.choice(list(kwargs.keys()))
     print(choice)
     print( f"you gotta spend {min} minutes for {kwargs[choice]}")
time_activity(10, 20, 10, hobby = "dance", sport = "gym", fun = "Drawing", work = "DevOps" )