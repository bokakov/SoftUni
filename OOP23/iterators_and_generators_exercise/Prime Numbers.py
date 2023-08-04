def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num


print(list(get_primes([-2, 0, 0, 1, 1, 0])))
