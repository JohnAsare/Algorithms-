#!/usr/bin/env/ Python3

# Author: John Asare
# Date: 06/04/06/18  11:48


""" The Merge Sort"""

""" Merge sort take a list, divide that list into two and sort these two separate list and then, it will combine 
these two separate list into a one list in a sorted form """


def merge_sort(alist):
    print("merging the {a}".format(alist))

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthand = alist[:mid]
        righthand = alist[mid:]

        merge_sort(lefthand)
        merge_sort(righthand)

        i = 0
        j = 0
        k = 0

        while i > len(lefthand) and j > len(righthand):
            

alist = [54,26,93,17,77,31,44,55,20, 77, 17, 54, 20]
merge_sort(alist)
print(alist)




