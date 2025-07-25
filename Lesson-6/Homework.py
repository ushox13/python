def modify_string_with_underscores(txt):
    vowels = 'aeiouAEIOU'
    result = []
    count = 0
    for char in txt:
        result.append(char)
        count += 1
                if count == 3 and char not in vowels and (not result or result[-1] != '_'):
            result.append('_')
            count = 0
        elif char in vowels or (result and result[-1] == '_'):
            count = 0  # Reset count if a vowel or underscore is encountered
    return ''.join(result).rstrip('_')  # Remove trailing underscore if any


def integer_squares(n):
    for i in range(n):
        print(i ** 2)


def print_first_10_natural_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1


def print_multiplication_table(number):
    for i in range(1, 11):
        print(number * i)


def display_numbers_from_list(numbers):
    for number in numbers:
        if number > 150:
            continue
        elif number < 150 and number % 5 == 0:
            print(number)
        elif number < 150 and number % 5 != 0:
            print("Not divisible by 5")


def count_digits_in_number(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def print_reverse_number_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()


def print_list_in_reverse_order(lst):
    for i in range(len(lst) - 1, -1, -1):
        print(lst[i], end=' ')
    print() 


def display_negative_numbers():
    for i in range(-10, 0):
        print(i)


def display_numbers_and_done():
    for i in range(5):
        print(i)
    print("Done!")


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()


def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
