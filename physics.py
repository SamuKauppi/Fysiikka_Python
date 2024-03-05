from classes import Object
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from math import sin, cos, radians

xoffset = 2
yoffset = 30

# First object dimensions
object1 = [[0.5, 2.0], [-2.0, 2.0], [-2.0, -2.0], [0.5, -2.0], [3.0, 0.0]]

# Movement
v0 = 17.0   # 10 m/s
angle = 45
vx = v0 * cos(angle)
vy = v0 * sin(angle)
g = 9.81    # gravity
t = 0.0     # time
dt = 0.1    # delta time

# Rotation
wv = 90           # radians(deg)/s
dr = wv * dt        # radians

# determine object
obj1 = Object(xoffset, yoffset, v0, angle, wv, object1, dt, 0.95, 0.03)

# polygon
polygons = []

# First triangle
p = Polygon(obj1.object)
Polygon.set_fill(p, False)
polygons.append(p)

while t < 15:

    obj1.hits_ground()
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
xpoints = [0.1, 0.1]
ypoints = [boundsx[0], boundsx[1]]

plt.plot(ypoints, xpoints, color = 'r')
# show plot
plt.show()
