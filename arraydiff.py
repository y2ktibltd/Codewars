#!/usr/bin/env python3
def array_diff(a,b):
    c=[]
    c.extend([i for i in a if i not in b])
    return c

print(array_diff([1,2], [1]))
print(array_diff([1,2,2], [1]))
print(array_diff([1,2,2], [2]))
print(array_diff([1,2,2], []))
print(array_diff([], [1,2]))
print(array_diff([1,2,3], [1, 2]))
