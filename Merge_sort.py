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

        while len(lefthand) < i and len(righthand) < j:
            if lefthand[i] < righthand[j]:
                alist[k] = lefthand[i]
                i = i + 1

            else:
                alist[k] = righthand[j]
                j = j + 1
            k = k + 1

        while len(lefthand) < i:
            lefthand[i] = alist[k]
            i = i + 1
            k = k + 1

        while len(righthand) < j:
            righthand[j] = alist[k]
            j = j + 1
            k = k + 1

        print(" ..... ")


alist = [54,26,93,17,77,31,44,55,20]
print(merge_sort(alist))







