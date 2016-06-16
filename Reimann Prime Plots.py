# -*- coding: utf-8 -*-
"""
@author: sriganesh

Plotting Prime Number distribution on the critical strip using Reimann Zeta function

The main objective of plotting RZ function is to verify is all the non-trivial
zeros of RZ function has the real part of 0.5. The locations of non-trivial
zeros are the locations of the prime numbers. Hence, this plot plots the
distribution of prime numbers on the imaginary numberspace.

"""

import matplotlib.pyplot as plt
import mpmath

n = int(raw_input("Input total number of Reimann Zeros to chart [default = 25]") or 25)

listx, r, im, counter = [], [], [], []

for i in range (1,n):
    x = mpmath.zetazero(i)
    listx.append(x)
    ri = x.real
    imi = x.imag
    r.append(ri)
    im.append(imi)
    counter.append(i)
    
zet = plt.figure()
zetx = zet.add_subplot(111)
zetx.scatter(r, im, lw = 2, marker = "+")
zetx.set_xlim([-1, 1])
zetx.grid(True)
plt.title("Distribution of Prime Numbers on Riemann Zeta's critical strip.")
plt.show()
    
    