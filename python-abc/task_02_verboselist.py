#!/usr/bin/python3
"""2.Extending the Python List Notifications"""

class VerboseList(list):
    """Class VerboseList inheriting from list (inbuilt class)"""
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list")
    
    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items")

    def remove(self, value):
        print(f"Removed {value} from the list")    
        super().remove(value)

    def pop(self, index = -1):
        if index is None:
            super().pop(index)
            print(f"Popped {index} from the list")
