#!/usr/bin/env python3
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i])==sum(arr[i+1:]):
            return i
    return -1

print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([1,100,50,-51,1,1]))
print(find_even_index([1,2,3,4,5,6]))
print(find_even_index([20,10,30,10,10,15,35]))
print(find_even_index([20,10,-80,10,10,15,35]))
print(find_even_index([10,-80,10,10,15,35,20]))
print(find_even_index(list(range(1,100))))
print(find_even_index([0,0,0,0,0]))
print(find_even_index([-1,-2,-3,-4,-3,-2,-1]))
print(find_even_index(list(range(-100,-1))))
