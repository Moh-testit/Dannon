#!/usr/bin/env python3

import sys
from math import *

comparisons = 0
    
def parse(args):
    if len(args) != 1:
        print("Invalid number of arguments")
        sys.exit(84)
    if args [0] == "-h" or args[0] == "--help":
        print("USAGE\n\t./301dannon file\nDESCRIPTION\n\tfile\tfile that contains the numbers to be sorted, seperated by spaces\n")
        sys.exit(0)
    if len(args) != 1:
        print("Invalid number of arguments")
        sys.exit(84)
    file = open(args[0], 'r').read()
    val = ""
    for numb in file:
        if (numb.isdigit == False and numb.isdigit != '.' and numb.isdigit != '-'):
            if (val[-1] != ' '):
                val += " "
        else:
            val += numb
    array = val.split(' ') 
    return list(map(float, array))

def selection_sort(list):
    tmp = 0
    for i in range(len(list)):
        tmp += i
    return (tmp)

def insertion_sort(numb):
    count = 0
    for i in range(len(numb)):
        j = 0
        tmp = numb[i]
        while (j < i):
            count += 1
            if (tmp < numb[j]):
                break
            j += 1
        numb.insert(j, tmp)
        del numb[i + 1]
    return (count)

def bubble_sort(array):
    comparisons = 0

    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            comparisons += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return (comparisons)

def distribute_count(array, left, right):
    global comparisons
    pivot = array[0]

    for j in array[1:]:
        comparisons += 1
        if j < pivot:
            left.append(j)
        else:
            right.append(j)

def quick_sort(array):
    if len(array) > 1:
        L = []
        R = []
        distribute_count(array, L, R)
        quick_sort(L)
        quick_sort(R)
    return (comparisons)

def merge_sort(array): 
    if len(array) > 1: 
        i = j = k = comparisons = 0
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
  
        comparisons += merge_sort(left) 
        comparisons += merge_sort(right) 
        while i < len(left) and j < len(right): 
            comparisons += 1
            if left[i] < right[j]: 
                array[k] = left[i] 
                i += 1
            else: 
                array[k] = right[j] 
                j += 1
            k += 1
        for i in range (i , len(left)): 
            array[k] = left[i] 
            i += 1
            k += 1 
        for j  in range (j, len(right)): 
            array[k] = right[j] 
            j += 1
            k += 1
        return (comparisons)
    return (0)

def main_print(array):

    print("%d element%s" % (len(array), 's' if len(array) != 1 else ''))
    result = selection_sort(array.copy())
    print("Selection sort: %d comparisons" % result)
    result = insertion_sort(array.copy())
    print("Insertion sort: %d comparisons" % result)
    result = bubble_sort(array.copy())
    print("Bubble sort: %d comparisons" % result)
    result = quick_sort(array.copy())
    print("Quicksort: %d comparisons" % result)
    result = merge_sort(array.copy())
    print("Merge sort: %d comparisons" % result)
 
sys.argv.pop(0)
try:
    array = parse(sys.argv)
except:
    sys.exit(84)
main_print(array)