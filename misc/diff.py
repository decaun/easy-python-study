#!/bin/python
l_1 = open("1.txt", "r").read().splitlines()
l_2 = open("2.txt", "r").read().splitlines()

def diff(list1, list2):
    c = set(list1).union(set(list2))
    d = set(list1).intersection(set(list2))
    return list(c - d)


for r in diff(l_1,l_2):
    print(r)