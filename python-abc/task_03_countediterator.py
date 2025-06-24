#!/usr/bin/python3
"""3.CoutnedIterator - Keeping Track of Iteration"""


class CountedIterator:
    def __init__(self, iteration):
        """
        Initialized class

        args:
            iterable - iteration of the input list
            count
        """
        self.iterable = iter(iteration)
        self.count = 0

    def get_count(self):
        """
        method get_count
        return counter
        """
        return self.count

    def __next__(self):
        """
        overriding next
        return item from the iteration list
        raise StopIteration when finished list
        """
        try:
            item = next(self.iterable)
            self.count += 1
            # print(self.count)
            # print(item)
            # print(self.iterable)
            return (item)
        except:
            raise StopIteration("No more items.")