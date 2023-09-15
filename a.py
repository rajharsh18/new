def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprimes(a, b):
    return gcd(a, b) == 1

n = 56
coprimes = [x for x in range(1, n) if are_coprimes(n, x)]

print("Co-primes of 56:", coprimes)
