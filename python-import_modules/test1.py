#!/usr/bin/python3
import sys

for i in dir(sys):
    if i[:1]=="_":
        print(i)
