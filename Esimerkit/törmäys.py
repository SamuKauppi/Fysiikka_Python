# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:42:09 2024

@author: kopuj
"""

import matplotlib.pyplot as plt


g = 9.81 # m/s^2
dt = 0.05 # s
e = 0.8

xlist = [ 0.0 ] # m
ylist = [ 2.0 ] # m
vx = 6.0 # m/s
vy = 8.0 # m/s

aika = 0.0 # s
maxaika = 3.0 # s

while aika < maxaika:
    if (ylist[-1] < 0.0 and vy < 0.0):
        vy = -e*vy
    else:
        vy -= g*dt
    xlist.append(xlist[-1] + vx*dt)
    ylist.append(ylist[-1] + vy*dt)
    aika += dt

plt.plot(xlist,ylist,"o")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()