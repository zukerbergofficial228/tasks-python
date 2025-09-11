"""
Task:
Given the total weight N and the average price M of two types of cutlets 
with prices K1 and K2, find the weight of each type.

Input:
N (total weight), M (average price), K1, K2

Output:
Two integers — the weight of each type.

Example:
Input:
32
285
300
200
Output:
24 8
"""

# Input values
n = int(input())   # total weight (N)
m = int(input())   # average price (M)
k1 = int(input())  # price of the 1st type
k2 = int(input())  # price of the 2nd type

# If prices come in reversed order (cheaper first, more expensive second),
# we swap them to ensure k1 > k2. Later we will swap the result back.
swapped = False
if k1 < k2:
    k1, k2 = k2, k1
    swapped = True

# Solve the system of equations:
#   x + y = N
#   k1*x + k2*y = M*N
# Derived formula:
#   x = (N * (M - k2)) / (k1 - k2)
x = (n * (m - k2)) // (k1 - k2)   # weight of type 1 (more expensive after swap)
y = n - x                         # weight of type 2 (cheaper after swap)

# If we swapped prices before, swap back the results to keep the original order
if swapped:
    x, y = y, x

# Output: weights of the first and second type
print(x, y)
