#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
    language that combines remarkable power with very clear syntax"
str = str[39:67].strip() + str[109:115] + str[0:6].strip()
print(str)
