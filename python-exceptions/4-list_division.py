#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # my_list_1 = [10, 8, 4]
    # my_list_2 = [2, 4, 0, "H", 5]
    #list_length = max(len(my_list_1), len(my_list_2))
    total_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            result = 0
            print("out of range")
        except (TypeError, NameError):
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        finally:  # finally overrides all other excepts
            total_list.append(result)
    return (total_list)
