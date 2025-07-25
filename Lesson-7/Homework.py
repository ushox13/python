def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def digit_sum(k):
    return sum(int(digit) for digit in str(k))



def powers_of_two(N):
    k = 0
    while True:
        power = 2 ** k
        if power > N:
            break
        print(power)
        k += 1
