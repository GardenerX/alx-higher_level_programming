#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            new += elements
    return new