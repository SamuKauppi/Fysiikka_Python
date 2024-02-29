import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from math import sin, cos, radians

xoffset = 10
yoffset = 30

# Starting coordinates of our triangle
triangle = [[2.0, 0.0], [-1.0, 3.0], [-1.0, -3.0]]
for p in triangle:
    p[0] += xoffset
    p[1] += yoffset

# Center
cmx = 1/3 * (triangle[0][0] + triangle[1][0] + triangle[2][0])
cmy = 1/3 * (triangle[0][1] + triangle[1][1] + triangle[2][1])

# Triangle at origo
triangle_at_origo = [
        [triangle[0][0] - cmx, triangle[0][1] - cmy],
        [triangle[1][0] - cmx, triangle[1][1] - cmy],
        [triangle[2][0] - cmx, triangle[2][1] - cmy]
    ]
cm = [
    [cmx, cmy]
    ]
# 

# Movement
v0 = 17.0   # 10 m/s
angle = radians(45)
vx = v0 * cos(angle)
vy = v0 * sin(angle)
g = 9.81    # gravity
t = 0.0     # time
dt = 0.2    # delta time

# Rotation
wv = radians(-100)           # radians(deg)/s
dr = wv * dt

# polygon
polygons = []

# First triangle
p = Polygon(triangle)
Polygon.set_fill(p, False)
polygons.append(p)

while t < 3.5:

    # Center of mass position
    cmx = cm[-1][0] + vx * dt
    vyl = vy - g*dt
    cmy = cm[-1][1] + vyl * dt
    cm.append([cmx, cmy])

    new_triangle = [[], [], []]
    for i in range(3):

        rotx = triangle_at_origo[i][0] * cos(dr) - triangle_at_origo[i][1] * sin(dr)
        roty = triangle_at_origo[i][0] * sin(dr) + triangle_at_origo[i][1] * cos(dr)

        
        new_triangle[i] = [
            cm[-1][0] + rotx,
            cm[-1][1] + roty
            ]
        
        triangle_at_origo[i][0] = rotx
        triangle_at_origo[i][1] = roty


    p = Polygon(new_triangle)
    Polygon.set_fill(p, False)
    polygons.append(p)

    t += dt
    vy = vyl


ax = plt.gca()

for p in polygons:
    ax.add_patch(p)

# Determine plot area size
ax.set_xlim(-5,60)
ax.set_ylim(-5,50)
ax.set_aspect('equal')

# show plot
plt.show()
