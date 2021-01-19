# -*- coding: utf-8 -*-
"""
@author: sriganesh

Plotting the Reimann Zeta function map in imaginary numberspace.

"""

import mpmath
import matplotlib
import matplotlib.pyplot as plt
import timeit


points = int(input("Enter number of points: "))

plt.figure(figsize=(10,7))
start = timeit.default_timer()


#This will take a long time to run. For a short run, reduce points to 1000.
mpmath.cplot(mpmath.zeta, [-10, 10], [0, 100], points = points, verbose=False)


stop = timeit.default_timer()
print('Total run time: ', stop - start, "seconds")

