
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# Coordinates of our triangle
pts = np.array([[2,2], [2,4], [4,2]])
p = Polygon(pts)
Polygon.set_fill(p, False)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(1,7)
ax.set_ylim(1,8)
plt.show()
