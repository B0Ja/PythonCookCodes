# -*- coding: utf-8 -*-
"""
Created on Mon May 23 12:46:50 2016

@author: sriganesh

Objective: To check if all the numbers of the number lines give the (3n+1) result as even.

This is actually rudimentary as:

odd * constant = odd
even * constant = even

Therefore odd*constant + 1 is always even. Proof below.

"""

print ("Calculation to check if 3n+1 is even")
Maximum_range = int(raw_input("Maximum range for calculation: ") or 10000)

count = 0
for number in xrange(1, Maximum_range+1):
    if number % 2 == 1:
        if ((3*number)+1) % 2 == 1:
            print ("3n + 1 is not even!!")
            print ("3n + 1 for %d is %d") % number, (3*number+1)
            count += 1
            break
    else:
        if number < 100000000:
            if number % 1000000 == 0:
                print ("Number of (3*(odd) +1 != Even) for number upto %d is: %d" % (number, count))
        if number < 1000000000:
            if number % 10000000 == 0:
                print ("Number of (3*(odd) +1 != Even) for number upto %d is: %d" % (number, count))                
        