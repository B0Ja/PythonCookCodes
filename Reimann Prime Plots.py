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

n = int(input("Input total number of Reimann Zeros to chart [default = 25]") or 25)

listx, r, im, counter = [], [], [], []

for i in range (1,n):
    x = mpmath.zetazero(i)
    listx.append(x)
    ri = x.real
    imi = x.imag
    r.append(ri)
    im.append(imi)
    counter.append(i)
    
    
zet = plt.figure(figsize=(10,10))
zetx = zet.add_subplot(111)
zetx.scatter(r, im, lw = 2, marker = "o", color='tab:red')
zetx.set_xlim([-1, 1])
zetx.grid(True, linestyle='dashed', color='tab:gray', alpha=0.5)

plt.title("Distribution of Prime Numbers on Riemann Zeta's critical strip.", loc='center', color='k', fontsize=12)
plt.show()
    
    
