"""  Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

inp = input('Enter sentence: ').replace(' ', '')

alpha_count = 0
num_count = 0

for c in inp:
    if c.isalpha():
        alpha_count += 1
    elif c.isdigit():
        num_count += 1

print(f'LETTERS {alpha_count}')
print(f'DIGITS {num_count}')
