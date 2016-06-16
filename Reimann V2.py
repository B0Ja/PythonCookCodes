# -*- coding: utf-8 -*-
"""
@author: sriganesh /Brijesh Janardhanan

Plotting the Reimann Zeta function map in imaginary numberspace.

"""

import mpmath
import matplotlib

#This will take a long time to run. For a short run, reduce points to 1000.
mpmath.cplot(mpmath.zeta, [-10, 10], [0, 100], points = 5000, verbose=False)