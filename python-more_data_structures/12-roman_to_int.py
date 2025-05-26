#!/usr/bin/python3
def roman_to_int(roman_string):
    r_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    # roman_string = "MXC" #14
    if type(roman_string) is not str or roman_string is None:
        return (0)

    _sum = 0
    last_char = "I"
    rev_str = reversed(roman_string)
    # print(list(rev_string))
    # print(list(roman_string))

    for curr_char in rev_str:
        if r_dict[curr_char] >= r_dict[last_char]:
            # print("_sum {} + curr_letter {}".format(_sum, r_dict[curr_char]))
            _sum = _sum + r_dict[curr_char]
        elif r_dict[curr_char] < r_dict[last_char]:
            # print("_sum {} - curr_char {}".format(_sum, r_dict[curr_char]))
            _sum = _sum - r_dict[curr_char]
        last_char = curr_char
        # print(_sum)
    return (_sum)
