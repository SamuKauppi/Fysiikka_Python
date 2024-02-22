
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# Coordinates of our triangle
pts = np.array([[3,3], [2,5], [5,2]])
p = Polygon(pts)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(1,7)
ax.set_ylim(1,8)
plt.show()
