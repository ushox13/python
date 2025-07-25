from datetime import date
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: ")
current_year = date.today().year
age = current_year - year_of_birth
print(f"Hello {name}, you are {age} years old.")


txt = 'LMaasleitbtui'
car_names = txt.split('L')[1:]  # Split by 'L' and ignore the first empty element
print("Car names:", car_names)


txt = 'MsaatmiazD'
car_names = txt.split('M')[1:]  # Split by 'M' and ignore the first empty element
print("Car names:", car_names)


txt = "I'am John. I am from London"
residence_area = txt.split('from ')[1]  # Split by 'from ' and take the second part
print("Residence area:", residence_area)


user_input = input("Enter a string: ")
reversed_string = user_input[::-1]  # Reverse the string using slicing  
print("Reversed string:", reversed_string)


user_input = input("Enter a string to count vowels: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in user_input if char in vowels)
print("Number of vowels:", vowel_count)


numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = list(map(int, numbers.split()))  


def is_palindrome(word):
    return word == word[::-1]
word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")   


email = input("Enter your email address: ")
domain = email.split('@')[1] if '@' in email else "Invalid email address"
print("Email domain:", domain)


import random
import string
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
