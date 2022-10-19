#!/usr/bin/env python3
def duplicate_count(text):
    return len([i for i in set(text.upper()) if text.upper().count(i)>1])

print(duplicate_count(""))
print(duplicate_count("abcde"))
print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))
