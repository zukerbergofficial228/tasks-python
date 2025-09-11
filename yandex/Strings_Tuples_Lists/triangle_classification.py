"""
Task:
Given three side lengths of a triangle, determine its type 
(acute, obtuse, or right-angled) using Pythagoras' theorem.

Rules:
- Right triangle  -> output "100%"
- Obtuse triangle -> output "large"
- Acute triangle  -> output "extremely small"
"""

# Read three side lengths
a = int(input())
b = int(input())
c = int(input())

# Sort sides so that c is always the largest (candidate for hypotenuse)
a, b, c = sorted([a, b, c])

# Apply Pythagoras' theorem to classify the triangle
if c**2 == a**2 + b**2:
    print("100%")
elif c**2 > a**2 + b**2:
    print("large")
else:
    print("extremely small")

