# Python Basics Learning Summary

A comprehensive guide covering fundamental Python concepts, syntax, and programming techniques for beginners.

### Data Types

#### Basic Data Types
```python
# Integers
age = 25
count = -10

# Floats
price = 19.99
temperature = -5.5

# Strings
name = "John"
message = 'Hello World'
multiline = """This is a
multiline string"""

# Booleans
is_active = True
is_completed = False

# None (null value)
result = None
```

#### Type Checking and Conversion
```python
# Check type
print(type(age))  # <class 'int'>
print(isinstance(price, float))  # True

# Type conversion
str_num = "123"
num = int(str_num)  # Convert to integer
float_num = float(str_num)  # Convert to float
str_from_num = str(num)  # Convert to string
```

### Variables and Constants

#### Variable Assignment
```python
# Single assignment
x = 10
name = "Alice"

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0

# Swapping variables
a, b = b, a
```

#### Naming Conventions
```python
# Good variable names
user_name = "john_doe"
total_price = 99.99
is_valid = True

# Constants (by convention, use UPPERCASE)
PI = 3.14159
MAX_SIZE = 100
DEFAULT_COLOR = "blue"
```

### Strings

#### String Operations
```python
text = "Hello World"

# Length
print(len(text))  # 11

# Indexing
print(text[0])    # 'H'
print(text[-1])   # 'd'

# Slicing
print(text[0:5])  # 'Hello'
print(text[6:])   # 'World'
print(text[:5])   # 'Hello'

# Common methods
print(text.upper())      # 'HELLO WORLD'
print(text.lower())      # 'hello world'
print(text.replace('World', 'Python'))  # 'Hello Python'
print(text.split())      # ['Hello', 'World']
```

#### String Formatting
```python
name = "Alice"
age = 30

# f-strings (Python 3.6+)
message = f"My name is {name} and I'm {age} years old"

# format() method
message = "My name is {} and I'm {} years old".format(name, age)
message = "My name is {0} and I'm {1} years old".format(name, age)

# % formatting (older style)
message = "My name is %s and I'm %d years old" % (name, age)
```

### Lists

#### Creating and Accessing Lists
```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]
empty_list = []

# Accessing elements
print(fruits[0])    # 'apple'
print(fruits[-1])   # 'orange'
print(fruits[1:3])  # ['banana', 'orange']
```

#### List Methods
```python
fruits = ["apple", "banana"]

# Adding elements
fruits.append("orange")        # Add to end
fruits.insert(0, "grape")     # Insert at index
fruits.extend(["mango", "kiwi"])  # Add multiple

# Removing elements
fruits.remove("banana")        # Remove by value
popped = fruits.pop()         # Remove last and return
del fruits[0]                 # Delete by index

# Other useful methods
print(len(fruits))            # Length
print(fruits.count("apple"))  # Count occurrences
fruits.sort()                 # Sort in place
fruits.reverse()              # Reverse in place
```

### Dictionaries

#### Creating and Accessing Dictionaries
```python
# Creating dictionaries
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Accessing values
print(student["name"])           # 'John'
print(student.get("age"))        # 20
print(student.get("height", 0))  # 0 (default if key not found)
```

#### Dictionary Methods
```python
student = {"name": "John", "age": 20, "grade": "A"}

# Adding/updating
student["height"] = 175
student.update({"weight": 70, "age": 21})

# Removing
del student["grade"]
popped_value = student.pop("height", None)

# Useful methods
print(student.keys())     # dict_keys(['name', 'age', 'weight'])
print(student.values())   # dict_values(['John', 21, 70])
print(student.items())    # dict_items([('name', 'John'), ('age', 21), ('weight', 70)])

# Check if key exists
if "name" in student:
    print("Name exists")
```

### Tuples

#### Creating and Using Tuples
```python
# Creating tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma for single item
empty_tuple = ()

# Accessing elements (same as lists)
print(coordinates[0])  # 10
print(colors[1:3])     # ('green', 'blue')

# Tuples are immutable
# coordinates[0] = 5  # This would cause an error

# Tuple unpacking
x, y = coordinates
print(x, y)  # 10 20
```

### Sets

#### Creating and Using Sets
```python
# Creating sets
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}
empty_set = set()  # Note: {} creates an empty dict, not set

# Adding and removing
numbers.add(6)
numbers.remove(1)      # Raises error if not found
numbers.discard(10)    # No error if not found

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))         # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  # {3, 4}
print(set1.difference(set2))    # {1, 2}
```

### Conditional Statements

#### If-Elif-Else
```python
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Ternary operator
status = "adult" if age >= 18 else "minor"

# Multiple conditions
if age >= 18 and age <= 65:
    print("Working age")

if name == "admin" or name == "root":
    print("System user")
```

### Loops

#### For Loops
```python
# Loop through list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Loop with index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Loop through range
for i in range(5):      # 0 to 4
    print(i)

for i in range(1, 6):   # 1 to 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Loop through dictionary
student = {"name": "John", "age": 20}
for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key}: {value}")
```

#### While Loops
```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop with break and continue
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    if user_input == '':
        continue
    print(f"You entered: {user_input}")
```

### Functions

#### Defining and Calling Functions
```python
# Basic function
def greet():
    print("Hello!")

greet()  # Call the function

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Function with default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}"

print(greet_with_title("Smith"))        # Hello, Mr. Smith
print(greet_with_title("Jane", "Ms."))  # Hello, Ms. Jane
```

#### Advanced Function Features
```python
# Variable number of arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

# Keyword arguments
def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name="John", age=30, city="New York")

# Lambda functions
square = lambda x: x ** 2
print(square(5))  # 25

# List comprehension with lambda
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
```

### List Comprehensions

#### Basic List Comprehensions
```python
# Create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# Filter with condition
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4]

# Transform strings
words = ["hello", "world", "python"]
capitalized = [word.upper() for word in words]
print(capitalized)  # ['HELLO', 'WORLD', 'PYTHON']

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Error Handling

#### Try-Except-Finally
```python
# Basic error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This always executes")

# Raising exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

### File Handling

#### Reading and Writing Files
```python
# Writing to file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")

# Reading from file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending to file
with open("example.txt", "a") as file:
    file.write("\nThis is appended text.")

# Working with JSON
import json

data = {"name": "John", "age": 30}
with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
```

### Classes and Objects

#### Basic Class Definition
```python
class Person:
    # Class variable
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}"

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.have_birthday())
```

#### Inheritance
```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

student = Student("Charlie", 20, "S12345")
student.add_grade(85)
student.add_grade(92)
print(f"Average grade: {student.get_average()}")
```

### Modules and Packages

#### Importing Modules
```python
# Import entire module
import math
print(math.pi)
print(math.sqrt(16))

# Import specific functions
from math import pi, sqrt
print(pi)
print(sqrt(16))

# Import with alias
import datetime as dt
now = dt.datetime.now()

# Import all (not recommended)
from math import *

# Create your own module (save as mymodule.py)
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

# Then import it
# from mymodule import greet, PI
```

### Common Built-in Functions

#### Useful Built-in Functions
```python
# Input/Output
name = input("Enter your name: ")
print("Hello,", name)

# Math functions
numbers = [1, 5, 3, 9, 2]
print(max(numbers))    # 9
print(min(numbers))    # 1
print(sum(numbers))    # 20
print(abs(-5))         # 5
print(round(3.14159, 2))  # 3.14

# Type conversion
print(int("123"))      # 123
print(float("3.14"))   # 3.14
print(str(123))        # '123'
print(list("hello"))   # ['h', 'e', 'l', 'l', 'o']

# Iteration
print(enumerate(["a", "b", "c"]))  # Creates index-value pairs
print(zip([1, 2, 3], ["a", "b", "c"]))  # Pairs elements from multiple iterables

# Filtering
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

# Mapping
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25, 36]
```

### Basic Scripting Patterns

#### Command Line Arguments
```python
import sys

# Access command line arguments
if len(sys.argv) > 1:
    print(f"Hello, {sys.argv[1]}!")
else:
    print("Hello, World!")

# Usage: python script.py Alice
# Output: Hello, Alice!
```

#### Environment Variables
```python
import os

# Get environment variable
home_dir = os.getenv("HOME", "/default/path")
print(f"Home directory: {home_dir}")

# Set environment variable
os.environ["MY_VAR"] = "Hello World"
print(os.environ.get("MY_VAR"))
```

#### Simple Script Structure
```python
#!/usr/bin/env python3
"""
A simple Python script example.
"""

def main():
    """Main function of the script."""
    print("This is the main function")
    
    # Your script logic here
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"Sum of numbers: {total}")

if __name__ == "__main__":
    main()
```

### Best Practices

#### Code Style Guidelines
```python
# Use meaningful variable names
user_count = 10  # Good
x = 10          # Not so good

# Follow PEP 8 naming conventions
class MyClass:      # Class names in PascalCase
    pass

def my_function():  # Function names in snake_case
    pass

MY_CONSTANT = 100   # Constants in UPPERCASE

# Use docstrings
def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle.
    
    Returns:
        float: The area of the circle.
    """
    return 3.14159 * radius ** 2

# Keep functions small and focused
# Use list comprehensions when appropriate
# Handle exceptions properly
# Use context managers for file operations
```

### Quick Reference

#### Common Operations Cheat Sheet
```python
# String operations
s = "hello world"
s.upper(), s.lower(), s.title(), s.replace("world", "python")

# List operations
lst = [1, 2, 3]
lst.append(4), lst.extend([5, 6]), lst.insert(0, 0)

# Dictionary operations
d = {"a": 1, "b": 2}
d["c"] = 3, d.get("d", 0), d.keys(), d.values(), d.items()

# Loop patterns
for i in range(10):           # 0 to 9
for i, item in enumerate(lst): # with index
for key, value in d.items():  # dictionary

# Comprehensions
[x**2 for x in range(10)]              # List
{x: x**2 for x in range(10)}           # Dictionary
{x for x in range(10) if x % 2 == 0}   # Set

# File operations
with open("file.txt", "r") as f:
    content = f.read()
```

---

**Note**: This summary covers the fundamental concepts of Python programming. Practice these concepts regularly to build proficiency and explore the official Python documentation for more advanced topics.
