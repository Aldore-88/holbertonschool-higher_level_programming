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
    start_of_line = True

    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 1
            start_of_line = True

            while i < len(text) and text[i] == ' ':
                i += 1

        elif text[i] == ' ' and start_of_line:
            i += 1

        else:
            print(text[i], end="")
            if text[i] != ' ':
                start_of_line = False
            i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
