#!/usr/bin/python3
#def roman_to_int(roman_string):
roman_dict = {"M": 1000, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
roman_string = "XIV" #14
if type(roman_string) is not str or roman_string == None:
    print(0)

total = 0
i=-1
last_letter = "I"
rev_string = reversed(roman_string)
print(list(rev_string))
print(list(roman_string))

while roman_string: 
    print[roman_string[i]]

