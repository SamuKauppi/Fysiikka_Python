from classes import Object
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from math import sin, cos, radians

xoffset = 2
yoffset = 30

# Starting coordinates of our triangle
triangle = [[2.0, 0.0], [-1.0, 3.0], [-1.0, -3.0]]

# Movement
v0 = 17.0   # 10 m/s
angle = 45
vx = v0 * cos(angle)
vy = v0 * sin(angle)
g = 9.81    # gravity
t = 0.0     # time
dt = 0.2    # delta time

# Rotation
wv = -180           # radians(deg)/s
dr = wv * dt

obj1 = Object(xoffset, yoffset, v0, angle, wv, triangle, dt)

# polygon
polygons = []

# First triangle
p = Polygon(triangle)
Polygon.set_fill(p, False)
polygons.append(p)

while t < 3.5:

    # Center of mass position
    cm = obj1.get_new_cm()

    new_triangle = obj1.get_new_rotation()

    for p in new_triangle:
        p[0] += cm[0]
        p[1] += cm[1]

    poly = Polygon(new_triangle)
    Polygon.set_fill(poly, False)
    polygons.append(poly)

    t += dt


ax = plt.gca()

for p in polygons:
    ax.add_patch(p)

# Determine plot area size
ax.set_xlim(-5,50)
ax.set_ylim(-5,50)
ax.set_aspect('equal')

# show plot
plt.show()
