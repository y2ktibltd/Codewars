#!/usr/bin/env python3
def high_and_low(n):
    n=sorted([int(i) for i in n.split()])
    n=" ".join([str(n[-1]),str(n[0])])
    return n 

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
print(high_and_low("1 3 2"))
