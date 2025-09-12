"""
Greatest Common Divisor (GCD) of multiple numbers

Task:
Given a sequence of natural numbers, find their greatest common divisor (GCD).

Input:
A single line of space-separated integers.

Output:
A single integer — the GCD of all input numbers.
"""

# Read numbers from input
n = input().split()
n = [int(i) for i in n]

# Start with the first number
res = n[0]

# Iterate through the rest of the numbers
for i in range(1, len(n)):
    a, b = res, n[i]
    # Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    res = a

# Print the result
print(res)
