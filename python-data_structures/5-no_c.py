#!/usr/bin/python3
#def no_c(string):

string = "chicago"
new_string = ""
for i in string:
    if i != "c" and i != 'C':
        new_string = new_string + i
print(new_string)
