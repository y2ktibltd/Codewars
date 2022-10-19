#!/usr/bin/env python3
def narcissistic(v):
    s=0
    for _ in range(len(str(v))):
        s+=pow(int(str(v)[_]),len(str(v)))
    if s==v:return True
    else:return False

print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))
