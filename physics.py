from classes import Object, cross
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def handle_coll():
    return


# checks collision between a point and obj
def is_object_collision(obj, point):
 
    has_coll = True
    for i in range(len(obj)):

        i_next = i + 1
        if(i_next >= len(obj)):
            i_next = 0

        # get vector from this point to next point
        rox = obj[i_next][0] - obj[i][0]
        roy = obj[i_next][1] - obj[i][1]
        ro = [rox, roy, 0]

        # get vector from this point to point
        rpx = point[0] - obj[i][0]
        rpy = point[1] - obj[i][1]
        rp = [rpx, rpy, 0]

        rxp = cross(ro, rp)[2]

        if rxp < 0:
            return False
    
    return has_coll

# shared components
g = 9.81    # gravity
t = 0.0     # time
dt = 0.13    # delta time

# object1 dimensions
cmx = 2
cmy = 25
object1 = [[2.0, 2.0], [-2.0, 2.0], [-2.0, -2.0], [2.0, -2.0]]

# object1 dimensions
cmx2 = 150
cmy2 = 25
object2 = [[1.5, 1.5], [-1.5, 1.5], [-1.5, -1.5], [1.5, -1.5]]

# Movement1
v0 = 17.0   # 10 m/s
angle = 45
e = 0.7
j = 3
m = 0.5
wv = 100        # radians(deg)/s

# Movement2
v02 = -17.0   # 10 m/s
angle2 = -45
e2 = 0.75
j2 = 2
m2 = 0.25
wv2 = -100        # radians(deg)/s

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

run = True
while t < 15:

    # create a polygon and add it to list
    poly = Polygon(obj1.object)
    Polygon.set_fill(poly, False)
    polygons.append(poly)

    poly = Polygon(obj2.object)
    Polygon.set_fill(poly, False)
    Polygon.set_color(poly, 'red')
    polygons.append(poly)

    if run == False:
        break

    obj1.hits_ground([xpoints[1], ypoints[1]], [xpoints[0], ypoints[0]])
    obj1.update_position()

    obj2.hits_ground([xpoints[1], ypoints[1]], [xpoints[0], ypoints[0]])
    obj2.update_position()

    for point in obj1.object:
        if is_object_collision(obj2.object, point) == True:
            run = False
    
    for point in obj2.object:
        if is_object_collision(obj1.object, point) == True:
            run = False

    # TODO: 
    # - collision check toiseen objektiin
    # 
    
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
