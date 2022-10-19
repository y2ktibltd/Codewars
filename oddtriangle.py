#!/usr/bin/env python3
def row_sum_odd_numbers(n):
    return n **3
#    i,s=1,0
#    for h in range(n):
#        for w in range(h+1):
#            s+=i
#            i+=2
#        if h==n-1:return s
#        else:s=0

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(19))
print(row_sum_odd_numbers(41))
