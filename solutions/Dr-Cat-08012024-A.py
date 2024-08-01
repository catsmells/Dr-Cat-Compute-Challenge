from itertools import product
from sympy import isprime
def xx(limit):
    largest_prime = None
    for a, b, c in product(range(-limit, limit + 1), repeat=3):
        sum_cubes = a**3 + b**3 + c**3
        if isprime(sum_cubes):
            if largest_prime is None or sum_cubes > largest_prime:
                largest_prime = sum_cubes
    return largest_prime
# Set the limit for the range of a, b, c
limit = 30
largest_prime = xx(limit)
print(f"The largest prime expressible as the sum of three cubes is: {largest_prime}.")
