# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:42:09 2024

@author: kopuj
"""

import matplotlib.pyplot as plt
from math import sin, cos, radians

g = 9.81
dt = 0.1

xlist = [ 0.0 ]
ylist = [ 0.0 ]
v0 = 30
kulma = radians(45)
vx = v0 * cos(kulma)
vya = v0 * sin(kulma)

while xlist[-1] < 65:
    vyl = vya - g*dt
    xlist.append(xlist[-1] + vx*dt)
    ylist.append(ylist[-1] + (vya+vyl)/2*dt)
    vya = vyl

plt.plot(xlist,ylist,"o")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()