#!/usr/bin/python3

def multiple_returns(input_sentence):
    if input_sentence == "":
        return (0, None)
    output_tuple = (len(input_sentence), input_sentence[0])
    return (output_tuple)