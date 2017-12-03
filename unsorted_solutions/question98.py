"""  Question 98:

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
"""

# Generate combinations that sum up to 35 (x + y = 35)
heads = 35
legs = 94
partners = []

for i in range(1, heads - 1):
    partners.append((i, heads-i))

# Loop through the combinations and found which satisfies
# x + 2y = 47 or 2x + 4y = 94

for partner in partners:
    if partner[0] + (2 * partner[1]) == 47:
        print(partner)
    if (2 * partner[0]) + (4 * partner[1]) == legs:
        print('We have {} chickens and {} rabbits in the farm!'.format(partner[0], partner[1]))
