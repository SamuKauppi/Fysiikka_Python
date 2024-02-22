# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:42:09 2024

@author: kopuj
"""

import matplotlib.pyplot as plt
from math import sin, cos, radians, sqrt

g = 9.81 # m/s^2
dt = 0.05 # s
cpm = 0.02 # 1/m

xlist = [ 0.0 ]
ylist = [ 0.0 ]
v0 = 30 # m/s
kulma = radians(45) # asteet -> radiaanit
vx = v0 * cos(kulma)
vy = v0 * sin(kulma)

while ylist[-1] >= 0:
    ax = -cpm*sqrt(vx**2 + vy**2)*vx
    ay = -cpm*sqrt(vx**2 + vy**2)*vy - g
    vx += ax*dt
    vy += ay*dt
    xlist.append(xlist[-1] + vx*dt)
    ylist.append(ylist[-1] + vy*dt)

plt.plot(xlist,ylist,"o")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()