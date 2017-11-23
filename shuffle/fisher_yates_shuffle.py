import random


def shuffle(seq):
    for i in range(len(seq)-1, -1, -1):
        k = random.randint(0, i)
        temp = seq[i]
        seq[i] = seq[k]
        seq[k] = temp

text_twist = list("sunflower")
print(text_twist)
for x in range(11):
    shuffle(text_twist)
    print(text_twist)
