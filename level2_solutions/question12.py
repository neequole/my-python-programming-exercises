"""  Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

out = []

for num in range(1000, 3000):
    include = True
    num_str = str(num)
    for digit in num_str:
        if int(digit) % 2 != 0:
            include = False
            break
    if include:
        out.append(num_str)
print(', '.join(out))
