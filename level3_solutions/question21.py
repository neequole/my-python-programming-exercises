"""  Question 21
Level 3

Question
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps.
Please write a program to compute the distance from current position after a
sequence of movement and original point. If the distance is a float, then just
print the nearest integer.

Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
import math


def get_distance(to_position, from_position):
    return math.sqrt(((to_position[0]-from_position[0]) ** 2) + ((to_position[1] - from_position[1]) **2))


current_position = [0, 0]

while True:
    try:
        direction, steps = input("Enter movement: ").split()
    except (TypeError, ValueError) as e:
        break
    direction = direction.upper()
    steps = int(steps)
    if direction == 'UP':
        current_position[0] += steps
    elif direction == 'DOWN':
        current_position[0] -= steps
    elif direction == 'LEFT':
        current_position[1] += steps
    elif direction == 'RIGHT':
        current_position[1] -= steps

distance = round(get_distance(current_position, [0, 0]))
print(distance)
