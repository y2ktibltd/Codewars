#!/usr/bin/env python3
def strip_comments(strng,markers):
    res=""
    i=0
    if len(strng)==0:return"\n"
    while i < (len(strng)):
        if strng[i] not in markers:
            res+=strng[i]
        if strng[i] in markers:
            while strng[i]!="\n" and i<len(strng)-1:
                i+=1
            if strng[i]=="\n":i-=1
#            res=res.rstrip()
        i+=1
    return "".join(res)


print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])) # 'apples, pears\ngrapes\nbananas'
print(strip_comments('a #b\nc\nd $e f g', ['#', '$'])) # 'a\nc\nd'
print(strip_comments(' a #b\nc\nd $e f g', ['#', '$'])) # ' a\nc\nd'

