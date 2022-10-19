#!/usr/bin/env python3
from functools import cache
from sys import setrecursionlimit as rec
rec(100000)
@cache
def fibonacci(n):
    if n in [0,1]:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(7)) # 190392490709135)
print(fibonacci(70)) # 190392490709135)
print(fibonacci(60)) # 1548008755920)
print(fibonacci(50)) # 12586269025)
print(fibonacci(10000)) # 12586269025)
