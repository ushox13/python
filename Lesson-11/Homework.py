import math_operations
import string_utils


Create your own virtual environment and install some python packages.
Create custom modules.
Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)
Create custom packages.
Create geometry package.
 geometry\
     __init__.py
     circle.py
 Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
Create file_operations package.
 file_operations\
     __init__.py
     file_reader.py
     file_writer.py
 
Define read_file function in file_reader.py. This function accepts one argument(file_path). Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).


pip install numpy


def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def reverse_string(s):
    return s[::-1]
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


import math
def calculate_area(radius):
    return math.pi * radius ** 2
def calculate_circumference(radius):
    return 2 * math.pi * radius


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)



from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file
# Math operations
print("Add:", add(10, 5))
print("Divide:", divide(10, 2))
# String utilities
text = "Vanilla Sky"
print("Reversed:", reverse_string(text))
print("Vowel Count:", count_vowels(text))
# Geometry
radius = 5
print("Circle Area:", calculate_area(radius))
print("Circle Circumference:", calculate_circumference(radius))
# File operations
write_file("sample.txt", "Hello, this is a test file.")
print("Read from file:", read_file("sample.txt"))
