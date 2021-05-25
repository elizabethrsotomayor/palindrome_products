from itertools import product

from flask_sqlalchemy import xrange


def largest(min_factor: int, max_factor: int):
    """Return the largest palindromes which are products of numbers within a given range."""
    # multiples = ((a, b) for a, b in product(xrange(100, 999), repeat=2) if is_palindrome(a * b))
    # print
    # max(multiples, key=lambda (a, b): a * b)


def smallest(min_factor, max_factor):
    """Return the smallest palindromes which are products of numbers within a given range."""
    # print(min_factor, max_factor)

    num = min_factor
    fact = []
    value = 0

    possible_products = []

    number = 1
    for i in range(1, max_factor+1):
        for n in range(min_factor, max_factor+1):
            print(n*number)
        number += 1

    return min_factor, fact


value, factors = smallest(min_factor=1, max_factor=9)
print(value, factors)
        #self.assertEqual(value, 1)
        #self.assertFactorsEqual(factors, [[1, 1]])

""" Given the range [1, 9] (both inclusive)

And given the list of all possible products within this range: 
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 15, 21, 24, 27, 20, 28, 32, 36, 25, 30, 35, 40, 
     45, 42, 48, 54, 49, 56, 63, 64, 72, 81]

The palindrome products are all single digit numbers (in this case): 
[1, 2, 3, 4, 5, 6, 7, 8, 9]

The smallest palindrome product is 1. 
Its factors are (1, 1). The largest palindrome product is 9. Its factors are (1, 9) and (3, 3)."""