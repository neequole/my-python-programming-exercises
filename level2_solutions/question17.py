"""   Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

net_amount = 0

while True:
    try:
        action, amount = input("Enter new transaction log:").split()
    except ValueError:
        break
    else:
        action = action.upper()
        amount = float(amount)
        if action == 'D':
            net_amount += amount
        elif action == 'W':
            net_amount -= amount

print(net_amount)
