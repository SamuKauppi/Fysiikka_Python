from classes import Object
from collision import handle_coll, is_object_collision
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# shared components
g = 9.81    # gravity
t = 0.0     # time
dt = 0.13    # delta time

# object1 dimensions
cmx = 52
cmy = 25
object1 = [[2.0, 2.0], [-2.0, 2.0], [-2.0, -2.0], [2.0, -2.0]]

# object1 dimensions
cmx2 = 125
cmy2 = 25
object2 = [[2, 2], [-2, 2], [-2, -2], [2, -2]]

# Movement1
v0 = 20.0   # 10 m/s
angle = 45
e = 0.7
j = 3
m = 1
wv = 100        # radians(deg)/s

# Movement2
v02 = -20.0   # 10 m/s
angle2 = -45
e2 = 0.75
j2 = 3
m2 = 2
wv2 = 50        # radians(deg)/s

# determine object
obj1 = Object(cmx, cmy, v0, angle, wv, object1, dt, e, j, m)

obj2 = Object(cmx2, cmy2, v02, angle2, wv2, object2, dt, e2, j2, m2)

# polygon
polygons = []

# Determine plot area size
boundsx = [-5, 210]
boundsy = [-10, 60]   

# Determine ground size
ypoints = [-10, 5]
xpoints = [boundsx[0], boundsx[1]]

color1 = "red"
color2 = "black"

while t < 15:

    is_coll = False
    obj1_coll = False

    # check for collision in obj1
    for point in obj1.object:
        if is_object_collision(obj2.object, point) == True:
            is_coll = True
            coll_point = point
            obj1_coll = True


    # check for collision in obj2
    for point in obj2.object:
        if is_object_collision(obj1.object, point) == True:
            is_coll = True
            coll_point = point
            obj1_coll = False


    # if collsion happens, handle collsion
    if is_coll:
        obj1.is_coll = True
        obj2.is_coll = True

        color1 = "blue"
        color2 = "green"

        if obj1_coll == True:
            coll = handle_coll(obj2, obj1, coll_point)
            obj1.set_new_speeds(coll[1])
            obj2.set_new_speeds(coll[0])
        else:
            coll = handle_coll(obj1, obj2, coll_point)
            obj1.set_new_speeds(coll[0])
            obj2.set_new_speeds(coll[1])

    # Check for collisions with ground and update speeds if not colliding with other object
    else:
        obj1.hits_ground([xpoints[1], ypoints[1]], [xpoints[0], ypoints[0]])
        obj2.hits_ground([xpoints[1], ypoints[1]], [xpoints[0], ypoints[0]])

    # update positions
    obj1.update_position()
    obj2.update_position()

    # create a polygon and add it to list to be drawn
    poly = Polygon(obj1.object)
    Polygon.set_fill(poly, False)
    Polygon.set_color(poly, color2)
    polygons.append(poly)

    poly = Polygon(obj2.object)
    Polygon.set_fill(poly, False)
    Polygon.set_color(poly, color1)
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
