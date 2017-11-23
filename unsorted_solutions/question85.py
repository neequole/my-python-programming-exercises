"""  Question 85:

Please write a program to generate all sentences where subject is in
["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list."""

subject = ['I', 'You']
verb = ['Play', 'Love']
obj = ['Hockey', 'Football']

for s in subject:
    for v in verb:
        for o in obj:
            print(f'{s} {v} {o}')
