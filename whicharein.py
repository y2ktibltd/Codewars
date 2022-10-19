#!/usr/bin/env python3
def in_array(array1,array2):
    sorted_array2=(sorted([i for i in set(array2)]))
    answer=[]
    for i in array1:
        for _ in range(len(sorted_array2)):
           if i in sorted_array2[_]:
               if i not in answer:
                   answer.append(i)
    return(sorted(answer))

print(in_array(["live", "arp", "strong"],["lively", "alive", "harp", "sharp", "armstrong"]))
print(in_array(["arp", "mice", "bull"],["lively", "alive", "harp", "sharp", "armstrong"]))
