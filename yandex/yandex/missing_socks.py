# Task:
# You are given a wardrobe with different clothing items: pants, shirts, and socks.
# Each sock has a size and a color.
# Your task is to find all socks that are missing a pair (appear an odd number of times).
#
# Output:
# 1. The number of socks without a pair.
# 2. A list of these socks (size and color), sorted first by size, then by color.

# read number of clothing items
n = int(input())

# dictionary to count socks
# key = (size, color), value = number of occurrences
socks = dict()

# list to store unpaired socks
missing_socks = []

# read each clothing item
for _ in range(n):
    tip, size, color = input().split()  # tip = type ("sock"), size = size, color = color
    size = int(size)
    if tip == "sock":  # only count socks
        socks[(size, color)] = socks.get((size, color), 0) + 1

# find socks with an odd count → missing a pair
for key, value in socks.items():
    if value % 2 != 0:
        missing_socks.append(key)

# sort socks: first by size, then by color
missing_socks.sort()

# print number of unpaired socks
print(len(missing_socks))

# print each sock as "size color"
for size, color in missing_socks:
    print(size, color)
