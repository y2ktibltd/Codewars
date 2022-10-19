#!/usr/bin/env python3
def valid_parentheses(string):
    count=0
    if string.count("(")==0 and string.count(")")==0:return True
    if string.count("(")==string.count(")"):
        for i in string:
            if i=="(":count+=1
            if i==")":count-=1
            if count<0:return False
        if count==0:return True
    else:return False

print(valid_parentheses("  ("))     #False
print(valid_parentheses(")test"))   #False
print(valid_parentheses(""))        #True
print(valid_parentheses("hi())("))  #False
print(valid_parentheses("hi(hi)()"))#True
