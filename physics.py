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
dt = 0.2    # delta time

# Rotation
wv = -100           # radians(deg)/s
dr = wv * dt        # radians

# determine object
obj1 = Object(xoffset, yoffset, v0, angle, wv, object1, dt)

# polygon
polygons = []

# First triangle
p = Polygon(obj1.object)
Polygon.set_fill(p, False)
polygons.append(p)

while t < 10:

    obj1.update_position()
    obj1.hits_ground()
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
ax.set_xlim(-5,110)
ax.set_ylim(-5,50)
ax.set_aspect('equal')

# draw ground
x = [-10, 120]
y = [-0.1, 0.1]
plt.plot(x, y, marker = 'o', color = 'r')
# show plot
plt.show()
