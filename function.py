""""
-We use function for reusability
- eg:
   - Capitalize a string many many time 
   instead of doing that manual 
   it better to write it once and call it whnever we 
   need it
"""
"""
def adults(name,age):
    combine = f"Her name is {name} and she is {age} years old"
    return combine
name = input("what is your name: ")

print(adults(str(name),25))
"""

# def summ(arg):
#     x = 0 
#     for i in arg:
#         x = x + i
#     return x
# out = summ([1 ,2 , 3])

# print(out)

# Default argument

def greetings (MSG= "Morning"):
    print(f"Good {MSG}")
    print("Wellcome to the function")
greetings("Evening")
    