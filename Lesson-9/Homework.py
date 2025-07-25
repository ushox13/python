class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius


class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def age(self):
        from datetime import datetime
        birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        today = datetime.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack.")
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack.")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item, price):
        self.items.append((item, price))
    def remove_item(self, item):
        self.items = [i for i in self.items if i[0] != item]
    def total_price(self):
        return sum(price for _, price in self.items)


class StackWithDisplay:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack.")
    def is_empty(self):
        return len(self.items) == 0
    def display(self):
        return self.items


class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from empty queue.")
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Peek from empty queue.")


class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[account_number] = initial_balance
    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        self.accounts[account_number] += amount
    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        if self.accounts[account_number] < amount:
            raise ValueError("Insufficient funds.")
        self.accounts[account_number] -= amount
    def get_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        return self.accounts[account_number]
