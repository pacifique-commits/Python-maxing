# random is module and choice is method
import random
def nam_feeback(name, age):
    print(f"{name} is {age} years old")
    if (age> 50) and (age < 75):
        print("Above the limit")
    elif (age > 75) and (age < 90):
        print ("Damm super selected ")
    elif (age >= 90):
        print ("Gonna need to interview you")
    else:
        print("I do wanna see your face")
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



def nam_feeback(name, age):
    print(f"{name} is {age} years old")
    if (age> 50) and (age < 75):
        print("Above the limit")
    elif (age > 75) and (age < 90):
        print ("Damm super selected ")
    elif (age >= 90):
        print ("Gonna need to interview you")
    else:
        print("I do wanna see your face")
    
nam_feeback("Peter", 70)
nam_feeback("Peter", 100)
