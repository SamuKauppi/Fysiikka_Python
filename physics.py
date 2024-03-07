from classes import Object
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from math import sin, cos, radians

xoffset = 2
yoffset = 25

# First object dimensions
object1 = [[2.0, 2.0], [-2.0, 2.0], [-2.0, -2.0], [2.0, -2.0]]

# Movement
v0 = 17.0   # 10 m/s
angle = 45
g = 9.81    # gravity
t = 0.0     # time
dt = 0.1    # delta time
e = 0.8
j = 3
m = 0.5

# Rotation
wv = 10        # radians(deg)/s

# determine object
obj1 = Object(xoffset, yoffset, v0, angle, wv, object1, dt, e, j, m)

# polygon
polygons = []

# First triangle
p = Polygon(obj1.object)
Polygon.set_fill(p, False)
polygons.append(p)
# Determine plot area size
boundsx = [-5, 210]
boundsy = [-10, 60]   

# Determine ground size
ypoints = [0, 0]
xpoints = [boundsx[0], boundsx[1]]

while t < 15:

    obj1.hits_ground([xpoints[1], ypoints[1]], [xpoints[0], ypoints[0]])
    obj1.update_position()

    # TODO: 
    # - ground check
    # - nopeuden muutos
    # - kulmanopeuden muutos
    # - collision check
    # 

    # create a polygon and add it to list
    poly = Polygon(obj1.object)
    Polygon.set_fill(poly, False)
    polygons.append(poly)

    # increment time
    t += dt


ax = plt.gca()

for p in polygons:
    ax.add_patch(p)

# Determine plot area size
boundsx = [-5, 210]
boundsy = [-10, 60]   

ax.set_xlim(boundsx[0],boundsx[1])
ax.set_ylim(boundsy[0],boundsy[1])
ax.set_aspect('equal')

# draw ground

plt.plot(xpoints, ypoints, color = 'r')
# show plot
plt.show()
