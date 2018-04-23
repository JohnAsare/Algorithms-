#!/usr/bin/env Python 3

# Name: John Asare
# Date: Sun Apr 22 22:34

""" Merge sort and program made out of merge_sort"""


def merge_sort(alist):

    if len(alist) > 1:
        mid = len(alist)//2
        left_side_of_the_list = alist[:mid]
        right_side_of_the_list = alist[mid:]

        merge_sort(left_side_of_the_list)
        merge_sort(right_side_of_the_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_side_of_the_list) and j < len(right_side_of_the_list):
            if left_side_of_the_list[i] < right_side_of_the_list[j]:
                alist[k] = left_side_of_the_list[i]
                i = i + 1
            else:
                alist[k] = right_side_of_the_list[j]
                j = j + 1
            k = k + 1

        while i < len(left_side_of_the_list):
            alist[k] = left_side_of_the_list[i]
            i = i + 1
            k = k + 1

        while j < len(right_side_of_the_list):
            alist[k] = right_side_of_the_list[j]
            j = j + 1
            k = k + 1
print(" ...... ")


alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)
print(alist)





