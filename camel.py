#!/usr/bin/env python3
def to_camel_case(text):
    if text=="":text=" "

    text_split=text.replace('_','-').split('-')
    text_split_camel=""

    if text[0].isupper():
        text_split_camel=[e.replace(e,e.capitalize()) for e in text_split]

    if text[0].islower():
        text_split_camel=[e.replace(e,e.capitalize()) for e in text_split[1:]]
        text_split_camel.insert(0,text_split[0])

    return "".join(text_split_camel)

print(to_camel_case(""))
print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-stealth-warrior"))
print(to_camel_case("The_stealth_warrior"))
