#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 4, Task 01"""
import random
import time

def sequential_search(search_list, item):
    t0= time.clock()
    pos = 0
    found = False
    
    while pos < len(search_list) and not found:
        if search_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    t1 = time.clock() - t0
    return found, t1


def ordered_sequential_search(search_list, item):
    t0= time.clock()
    pos = 0
    found = False
    
    while pos < len(search_list) and not found:
        if search_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    t1 = time.clock() - t0
    return found, t1



def binary_search_iterative(arr, l, r, x): 
    t0= time.clock()
    while l <= r: 
  
        mid = l + (r - l)/2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    t1 = time.clock() - t0
    return False,t1



def binary_search_recursive (arr, l, r, x): 
    t0= time.clock()
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search_recursive(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search_recursive(arr, mid+1, r, x) 
  
    else: 
        t1 = time.clock() - t0
        return False,t1



def main():
    x = [500,100,10000]
    sequen_srch = []
    ordered_sequen_srch = []
    binry_srch_iterative = []
    binry_srch_recur = []
    for a in range(0,100):

	lst = random.sample(range(1, 100000),(random.SystemRandom()).choice(x))
	#print lst
	a,b = sequential_search(lst,-1)
	sequen_srch.append(b)
	lst.sort()
	c,d = ordered_sequential_search(lst,-1)
	ordered_sequen_srch.append(d)
	e,f = binary_search_iterative(lst,0, len(lst)-1,-1)
	binry_srch_iterative.append(f)
	g,h = binary_search_recursive(lst,0, len(lst)-1,-1)
	binry_srch_recur.append(h)

    print "Sequential Search took %{0}f seconds to run, on average".format(str(sum(sequen_srch)/100))
    print "Ordered Sequential Search took %{0}f seconds to run, on average".format(str(sum(ordered_sequen_srch)/100))
    print "Binary Iterative Search took %{0}f seconds to run, on average".format(str(sum(binry_srch_iterative)/100))
    print "Binary Recursive Search took %{0}f seconds to run, on average".format(str(sum(binry_srch_recur)/100))
    

  
if __name__== "__main__":
  main()



