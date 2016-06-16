# -*- coding: utf-8 -*-
"""
Created on Wed May 18 23:54:55 2016

@author: sriganesh

The Collatz Conjecture:

Collatz Conjecture, named after Lothar Collatz, states that any positive
integer, if it is even is halved, and if odd is multiplied by 3 and 1 added,
will eventually converge to 1.

Eg: If positive integer chosen is 10, then:
1. 10 / 2 = 5
2. 5 * 3 = 15 + 1 = 16
3. 16 / 2 = 8
4. 8 / 2 = 4
5. 4 / 2 = 1 

"""

import matplotlib.pyplot as plt
import numpy as np
import random
import time
import math
from collections import Counter

collatz_input = int(raw_input("Enter the starting number: ") or 2)
Max_loop = int(raw_input("Enter the maximum range of random integer [default = 100]: ") or 100)
MaxIteration = int(raw_input("How many iterations required? "))

## Process Start Time
start_time = time.time()

collatz_list = []
collatz_seq  = []
collatz_norm = []
Max_list = []
Halt_period = []
Even_index = []
Odd_index = []

for itern in xrange(0,MaxIteration):
    
    generation = 0
    collatz_number = collatz_input if itern == 0 else 0
    collatz_number = random.randint(2,Max_loop)
    
    while collatz_number != 1:
        collatz_number = (collatz_number / 2) if collatz_number % 2 == 0 else ((collatz_number * 3) +1)
        collatz_list.append(collatz_number)
        generation += 1
        #Adding Even-Odd Loop
        tempD = int(str(collatz_number)[-1:])
        if tempD % 2 == 0:
            Even_index.append(tempD)
        else:
            Odd_index.append(tempD)
        #Even-Odd loop ends
    if collatz_number == 1:
        print ("------------------------------------------------------")
        print ("The numbers in the Collatz sequence."),
        print collatz_list
        print ("Total numbers in the Collatz sequence: %d") % len(collatz_list)
        print ("Number of iterations: %d") % generation
        print ("Maximum number in the sequence: %d ") % max(collatz_list)
        Max_list.append(max(collatz_list))
        Max_norm_value = (max(collatz_list)/(max(collatz_list)*1.0))
        print ("The maximum normalised value for the sequence: %1.5f") % Max_norm_value
        print ("------------------------------------------------------")
    if collatz_number == 1:
        collatz_seq.append(collatz_list)
        Halt_period.append(len(collatz_list))
    #if collatz_number == 1:
        #plt.hold(True)
        #plt.plot (collatz_list)
        #plt.ylabel ("Collatz Sequence")
        #plt.show()
    if collatz_number == 1:
        collatz_list = []

        


for items in xrange(0, len(collatz_seq)):
    if items == 0:
        MaxLen = len(collatz_seq[0])
    for itemzz in range (1,len(collatz_seq)):
        if len(collatz_seq[itemzz]) > MaxLen:
            MaxLen = len(collatz_seq[itemzz])
        


collatz_seq_org = collatz_seq [:] #Deep Copy the original strings of C_Seq

for iters in xrange (0, len(collatz_seq)):
    if len(collatz_seq[iters]) < MaxLen:
        extr = MaxLen - len(collatz_seq[iters])
        extr_list = collatz_seq[iters]
        for iters1 in range(0, extr):
            extr_list.append(1)
      
collatz_seq_appended = collatz_seq #Storing the appended lists of C_Seq
normzr_list = collatz_seq          #For normalising calculations

for idx in range(0, MaxIteration):
    Max_num = max(collatz_seq[idx])
    #normzr_list = collatz_seq[idx]
    for i in range(0, len(collatz_seq[idx])):
        if len(collatz_seq[idx]) == 0:
            break
        else:
            normzr_list[idx][i] = ((collatz_seq[idx][i] -1) / ((Max_num -1)* 1.0))


## Plotting The Normalised Chart
x = np.arange(MaxLen)  # X-axis of the multi-plot    

for charts in range(0, MaxIteration):
    plt.hold(True)
    plt.plot(x, collatz_seq[charts])
    plt.title ("Collatz Sequences - Normalised ")
    plt.ylabel ("Normalised Values")
    plt.xlabel ("Number of iterations")
plt.show()

#Halting Period Plot
xHist = np.arange(len(Halt_period))
plt.hist(Halt_period, bins = math.ceil(math.sqrt(len(Halt_period))))
plt.title ("The Halting Period of Collatz Sequences")
plt.xlabel ("Number of Iterations per seqeunce")
plt.ylabel ("Number of Collatz Sequences")
plt.show()

#Checking for number of consecutive times 3n+1 are odds.
odd_calc = collatz_seq_org[:]
counter_final = []
counter = []

for itemz in xrange(0, len(odd_calc)):
    for listx in range (0, len(odd_calc[itemz])):
        count = 0
        if odd_calc[itemz][listx] % 2 == 1:
            count += 1
        counter.append(count)
    counter_final.append(max(counter))
            
if max(counter_final) == 1:
    print ("Maximum sequential odd-numbers is %d, proving 3n+1 is always even.") % max(counter_final)
else:
    print ("Proof that 3n + 1 is not even!") #Not going to happen.

#Checking for Total Odd and Even numbers
print ("------------------------------------------------------")
print ("Total Even-numbers in Collatz sequence: %d") % len(Even_index)
print ("Total Odd-numbers in Collatz sequence:  %d") % len(Odd_index)
print ("Even numbers outnumber the Odd numbers by %d") % (len(Even_index) -len(Odd_index))
print ("Note: Even numbers always outnumber Odd numbers. "), 
print ("More Even numbers make sequence convergent.")
print ("------------------------------------------------------")

g1 = Counter(Odd_index)
g2 = Counter(Even_index)
print ("Odd numbers: "),g1
print ("Even numbers: "), g2
print ("------------------------------------------------------")


#Checking for process end time
print ("Total program processing time: %s seconds") % (time.time() - start_time)
