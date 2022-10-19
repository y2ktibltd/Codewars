#!/usr/bin/env python3
def persistence(n):
    if n<9:return 0
    n=[int(i) for i in str(n)]
    t=1
    c=0
    while len(n)>1:
        for i in n:
            t*=i
        n=[int(i) for i in str(t)]
        c+=1
        t=1
    return c


print("answer is: ",persistence(39))  # 3
print("answer is: ",persistence(4))   # 0
print("answer is: ",persistence(25))  # 2
print("answer is: ",persistence(999)) # 4
