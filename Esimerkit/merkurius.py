import matplotlib.pyplot as plt
from math import sqrt

dt = 0.025 # (yksiköissä 58,3 vrk)


xlist = [0.31] # AU
ylist = [0]
vx = 0
vy = 1.98
time = 0.0

while time < 1.6:
    time += dt
    r = sqrt(xlist[-1]**2+ylist[-1]**2)
    ax = -xlist[-1]/r**3
    ay = -ylist[-1]/r**3
    vx = vx + ax*dt
    vy = vy + ay*dt
    xlist.append(xlist[-1]+vx*dt)
    ylist.append(ylist[-1]+vy*dt)

    
plt.plot(xlist,ylist,'o')
plt.xlabel("x (AU)")
plt.ylabel("y (AU)")