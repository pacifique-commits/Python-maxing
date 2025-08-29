#Variable Assignments
var1 = "Python"
var2 = 75 #integer
var3 = 3.14 # float

print(var1)
print(var2)
print(var3)

#Multiple Assignements
a = b = c = 56
print(a)
print(b)
print(c)

# Multiple Assignnemts with mutiple values
x, y, z,w = "Alpha","beta",12,3.45
print("The value of x is:", type(x))
print("The value of y is:", type(y))
print("The value of w is:", w)
print("The value of z is:", z)

#List / collection of multiple datatyples , enclosed in 
#square brackets
num1 = 56
list_str = ["DEVOPS", 7, num1]
print (list_str)

#Tuple - round bracket enclosed ,- immutable not editable
# its like a cd drive -read only 
tup1 = ("King","Queen", 12)
print (tup1)

#Dictionary -key vlue pairs - curly braces 
dict1 = {
    "Name": "Joe",
    "Age": 34,
    "City": "New York",
    "Hobby": "Eating"

}
print (dict1)


# Boolean - True or False 
x = True
y = False # used in cndt-nal statment
print ("The type of x is :", type(x))