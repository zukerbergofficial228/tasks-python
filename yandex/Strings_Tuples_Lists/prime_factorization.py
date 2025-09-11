"""
Prime Factorization

Task:
Given a natural number n, decompose it into prime factors and print them
as a product in non-decreasing order.

Input:
One integer n (n >= 2).

Output:
Prime factors of n separated by " * ".
"""

# Read input number
number = int(input())

# Start dividing from the smallest prime number
i = 2

# Continue until the number is reduced to 1
while number > 1:
    if number % i == 0:              # if divisible by i
        print(i, end="")             # print the factor
        number //= i                  # reduce the number
        if number > 1:                # if not the last factor
            print(" * ", end="")      # print multiplication sign
    else:
        i += 1                        # try next divisor
