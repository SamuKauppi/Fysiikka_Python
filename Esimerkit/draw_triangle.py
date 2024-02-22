import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from math import sin, cos, radians

# Coordinates of our triangle
triangle = [[0.0,0.0], [0.0,2.0], [2.0,0.0]]

cmx = 1/3 * (triangle[0][0] + triangle[1][0] + triangle[2][0])
cmy = 1/3 * (triangle[0][1] + triangle[1][1] + triangle[2][1])

cms = [
    [cmx, cmy]
]

v0 = 10.0   # 10 m/s
kulma = radians(45)
vx = v0 * cos(kulma)
vy = v0 * sin(kulma)

t = 0.0     # time
dt = 0.1    # delta time

ax = plt.gca()
while t < 2.0:
    t += dt
    cmxl = cms[-1][0] + vx * dt
    cmyl = cms[-1][1] + vy * dt

    cms.append([cmxl, cmyl])

    new_triangle = [
        [triangle[0][0] + cmxl, triangle[0][1] + cmxl],
        [triangle[1][0] + cmxl, triangle[1][1] + cmxl],
        [triangle[2][0] + cmxl, triangle[2][1] + cmxl]
    ]

    p = Polygon(new_triangle)
    Polygon.set_fill(p, False)
    ax.add_patch(p)

# Determine plot area size
ax.set_xlim(-5,20)
ax.set_ylim(-5,20)

# show plot
plt.show()
