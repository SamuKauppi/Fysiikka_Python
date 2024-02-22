import matplotlib.pyplot as plt
from math import sin, cos, radians

e = 0.75
g = 9.81  
dt = 0.1 

xlist = [0.0]
ylist = [0.0]
v0 = 60
kulma = radians(45)
vx = v0 * cos(kulma)
vy = v0 * sin(kulma)

k = 0.1  # Ilmanvastuksen kerroin

while xlist[-1] < 500:
    if ylist[-1] <= 0.0 and vy <= 0.0:
        vy *= -e
        ylist[-1] = 0.0
    else:
        resistance = k * (vx**2 + vy**2)**0.5

        vx -= (resistance / v0) * vx * dt
        vy -= (g + (resistance / v0) * vy) * dt

    xlist.append(xlist[-1] + vx * dt)
    ylist.append(ylist[-1] + vy * dt)

plt.plot(xlist, ylist)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()
