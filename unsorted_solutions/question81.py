"""  Question 81:

Please write a program to compress and decompress the string
"hello world!hello world!hello world!hello world!".

Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
"""
import zlib
import sys


s = b"hello world!hello world!hello world!hello world!"
c = zlib.compress(s)
print(c)
d = zlib.decompress(c)
print(d)
print(sys.getsizeof(s))
print(sys.getsizeof(c))
