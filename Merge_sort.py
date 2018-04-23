#!/usr/bin/env Python 3

# Name: John Asare
# Date: Sun Apr 22 22:34

""" Merge sort and program made out of merge_sort"""


def merge_sort(alist):

    if len(alist) > 1:
        mid = len(alist)//2
        lefthand = alist[:mid]
        righthand = alist[mid:]

        merge_sort(lefthand)
        merge_sort(righthand)

        i = 0
        j = 0
        k = 0

        while i < len(lefthand) and j < len(righthand):
            if lefthand[i] < alist[k]:
                alist[k] = lefthand[i]
                i = i + 1

            else:
                righthand[j] = alist[k]
            k = k + 1


