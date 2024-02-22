import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from math import sin, cos, radians

# Coordinates of our triangle
triangle = [[2.0, 0.0], [-1.0, 1.0], [-1.0, -1.0]]

cmx = 1/3 * (triangle[0][0] + triangle[1][0] + triangle[2][0])
cmy = 1/3 * (triangle[0][1] + triangle[1][1] + triangle[2][1])

cms = [
    [cmx, cmy]
    ]

new_triangle = [
        [triangle[0][0] + cms[-1][0], triangle[0][1] + cms[-1][1]],
        [triangle[1][0] + cms[-1][0], triangle[1][1] + cms[-1][1]],
        [triangle[2][0] + cms[-1][0], triangle[2][1] + cms[-1][1]]
    ]

v0 = 12.0   # 10 m/s
kulma = radians(65)
vx = v0 * cos(kulma)
vy = v0 * sin(kulma)

g = 9.81    # gravity
t = 0.0     # time
dt = 0.1    # delta time

ax = plt.gca()
p = Polygon(new_triangle)
Polygon.set_fill(p, False)
ax.add_patch(p)

while t < 2.0:

    cmx = cms[-1][0] + vx * dt
    vyl = vy - g*dt
    cmy = cms[-1][1] + vyl * dt

    cms.append([cmx, cmy])

    new_triangle = [
        [triangle[0][0] + cms[-1][0], triangle[0][1] + cms[-1][1]],
        [triangle[1][0] + cms[-1][0], triangle[1][1] + cms[-1][1]],
        [triangle[2][0] + cms[-1][0], triangle[2][1] + cms[-1][1]]
    ]

    p = Polygon(new_triangle)
    Polygon.set_fill(p, False)
    ax.add_patch(p)

    t += dt
    vy = vyl


# Determine plot area size
ax.set_xlim(-5,25)
ax.set_ylim(-5,25)

# show plot
plt.show()
