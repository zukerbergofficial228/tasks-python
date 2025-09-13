'''
Task: Friends of the Second Level

You are given a list of pairs of friends. Friendship is symmetric.

For each person, find their "second-level friends" — the friends of their friends,
excluding the person themselves and their direct friends.

Input format:
- Each line contains two names.
- Input ends with an empty line.

Output format:
- For each person, print the line:
  Person: Friend1, Friend2, ...
- Both people and friends must be printed in alphabetical order.
- No duplicates are allowed.
'''

ant = {}

# Read input until empty line
while (pairs := input()) != "":
    pairs = pairs.split()
    if pairs[0] not in ant:
        ant[pairs[0]] = set()
    if pairs[1] not in ant:
        ant[pairs[1]] = set()
    ant[pairs[0]].add(pairs[1])
    ant[pairs[1]].add(pairs[0])

res = {}

# Build second-level friends
for x, z in ant.items():
    additional = set()
    for i in z:
        adding = ant[i].copy()
        adding.discard(x)        # remove the person themselves
        additional |= adding
    additional -= z              # remove direct friends
    res[x] = additional

# Print result
for i in sorted(res):
    print(f"{i}: {', '.join(sorted(res[i]))}")
