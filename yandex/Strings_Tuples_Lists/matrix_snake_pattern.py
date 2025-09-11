"""
Number Snake (row-wise)

Task:
Given height N and width M, print numbers from 1 to N*M in a "snake":
left→right on even rows (0-based), right→left on odd rows.
All columns must have equal width (based on N*M).

Input:
N
M

Output:
N rows of M numbers, snake pattern.
"""

N = int(input())
M = int(input())

width = len(str(N * M))  # column width

for i in range(N):
    row = []
    if i % 2 == 0:
        # left to right
        for j in range(M):
            row.append(f"{i*M + j + 1:>{width}}")
    else:
        # right to left
        for j in range(M):
            row.append(f"{i*M + (M - 1 - j) + 1:>{width}}")
    print(" ".join(row))
