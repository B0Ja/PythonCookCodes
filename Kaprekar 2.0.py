# -*- coding: utf-8 -*-
"""
Created on Fri May 27 16:40:11 2016

@author: sriganesh

Kaprekar's Constant

"""
#Get the user input for number
number = raw_input("Enter four-digit number: ")

#Convert to String
numberstr = str(number)

x = int("".join(sorted(numberstr, reverse = False)))
y = int("".join(sorted(numberstr, reverse= True)))

count = 0
z = 0

if len (numberstr) > 4:
    print "Kaprekar's initial criterion of maximum digits not met."
elif len (numberstr) < 3:
    print "Kaprekar's initial criterion of minimum digits not met."
else:
    if len(numberstr) == 3:
        numberstr = numberstr.rjust(4, "0")
    if len (numberstr) == 4:
        x = int("".join(sorted(numberstr, reverse = False)))
        y = int("".join(sorted(numberstr, reverse= True)))
        while z != 6174:
            z = y - x
            z_str = str(z)
            print ( "%d - %d = %d") %(x, y, z)
            x = int("".join(sorted(z_str, reverse = False)))
            y = int("".join(sorted(z_str, reverse= True)))
            count += 1
            
if z == 6174:
    print ("The final value is %d, verifying Kaprekar's constant." %z)
    print ("Number of iterations to converge: %d" %count)
     
    

    