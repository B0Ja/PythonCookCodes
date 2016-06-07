# -*- coding: utf-8 -*-
"""
Created on Fri May 13 22:57:23 2016

@author: sriganesh

STRING-MATCH

PS: This program is based on one of book-programs, unfortunately I don't remember which book. Suffice to say its not a completely original creation.
"""

import string
import random
import time

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

target = raw_input("Enter your target text: ")
attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
attemptNext = ''

completed = False
generation = 0

while completed == False:
    print(attemptThis)
    attemptNext = ''
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += target[i]
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.1)

print("Target matched! That took " + str(generation) + " generation(s)")
