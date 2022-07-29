def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if not x % i:
            return False
    return True