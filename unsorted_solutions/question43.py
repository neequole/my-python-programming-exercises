"""  Question 43:
Write a program which accepts a string as input to print "Yes" if the string is
"yes" or "YES" or "Yes", otherwise print "No".

Hints:
Use if statement to judge condition.
"""

inp = input("Are you a fan? ")
if inp in ["yes", "YES", "Yes"]:
    print("Yes")
else:
    print("No")
