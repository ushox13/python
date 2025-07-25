def is_leap(year):
    """Determines whether a given year is a leap year.
    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.
    Parameters:
    year (int): The year to be checked.
    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == "__main__":
    print(is_leap(2020))  # True
    print(is_leap(1900))  # False
    print(is_leap(2000))  # True
    print(is_leap(2021))  # False


def check_weird(n):
    """Checks whether a number is weird based on given conditions.
    Parameters:
    n (int): The number to be checked.
    Returns:
    str: "Weird" or "Not Weird" based on the conditions.
    """
    if n % 2 == 1:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    elif n > 20:
        return "Not Weird"
    else:
        return "Invalid input"
