#!/usr/bin/python3
"""5-text indent"""


def text_indentation(text):
    """Print text with 2 newlines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 1
            
            while i < len(text) and text[i] == ' ':
                i += 1
                
        elif text[i] == ' ' and (i == 0 or i == len(text) - 1):
            i += 1
            
        else:
            print(text[i], end="")
            i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
