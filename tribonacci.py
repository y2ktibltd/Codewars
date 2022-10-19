#!/usr/bin/env python3
def tribonacci(sig,n):
    if n==0:return []
    if n<3:return sig[:n]

    for _ in range(n-len(sig)):
        sig.append(sig[-3]+sig[-2]+sig[-1])
    return sig

print(tribonacci([1, 1, 1], 10))
print(tribonacci([0, 0, 1], 10))
print(tribonacci([0, 1, 1], 10))
print(tribonacci([1, 0, 0], 10))
print(tribonacci([0, 0, 0], 10))
print(tribonacci([1, 2, 3], 10))
print(tribonacci([3, 2, 1], 10))
print(tribonacci([1, 1, 1], 1))
print(tribonacci([300, 200, 100], 0))
print(tribonacci([0.5, 0.5, 0.5], 30))
