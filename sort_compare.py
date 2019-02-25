#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 4, Task 02"""
import time
import copy
import random

# Function to do insertion sort 
def insertion_sort(arr): 
    t0= time.clock()
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
    return time.clock() - t0


def shell_sort(arr):
    t0= time.clock()
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n/2
  
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap /= 2
    return time.clock() - t0

def python_sort(arr):
    t0= time.clock()
    arr.sort()
    t1 = time.clock() - t0
    return t1


def main():
    x = [500,100,10000]
    ins_srt = []
    shell_srt = []
    pyt_srt = []

    for each in x:

	lst = random.sample(range(1, 100000),each)
	shell_lst = copy.deepcopy(lst)
	python_lst = copy.deepcopy(lst)
	a = insertion_sort(lst)
	ins_srt.append(a)
	d = shell_sort(shell_lst)
	shell_srt.append(d)
	f = python_sort(python_lst)
	pyt_srt.append(f)
	

    print "Insertion Sort took %{0}f seconds to run, on average".format(str(sum(ins_srt)/3))
    print "Shell Sort took %{0}f seconds to run, on average".format(str(sum(shell_srt)/3))
    print "Python Sort took %{0}f seconds to run, on average".format(str(sum(pyt_srt)/3))

    

  
if __name__== "__main__":
  main()


