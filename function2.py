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
