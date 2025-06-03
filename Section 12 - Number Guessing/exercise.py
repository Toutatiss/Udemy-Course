def is_prime(num):
    is_prime = True
    for number in range(num - 1, 1, -1):
        if num % number == 0:
            is_prime = False
    return is_prime

print(is_prime(4))
