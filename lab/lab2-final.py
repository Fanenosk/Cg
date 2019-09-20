from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np


fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = Axes3D(fig)


# Вершины

v = np.array([[0, 0, 0], [1, 0, 2], [4, 0, 2], [3, 0, 0],
              [0, 2, 0], [1, 2, 2], [4, 2, 2], [3, 2, 0],
              ])


ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# projections

ax.plot([0, 1, 4, 3, 0], [0, 2, 2, 0, 0], 'b', zdir='y', zs=3)

ax.plot([0, 0, 2, 2, 0], [0, 2, 2, 0, 0], 'b', zdir='x', zs=-1)

ax.plot([0, 0, 4, 4, 0], [0, 2, 2, 0, 0], 'b', zdir='z', zs=-1)


# shape
verts = [[v[0], v[1], v[2], v[3]],
         [v[4], v[5], v[6], v[7]],
         [v[0], v[1], v[5], v[4]],
         [v[2], v[3], v[7], v[6]],
         [v[1], v[2], v[6], v[5]],
         [v[4], v[7], v[3], v[0]],
         [v[2], v[3], v[7], v[6]]]

fig = Poly3DCollection(
    verts)
#	alpha=.25)

fig.set_facecolor('cyan')
fig.set_edgecolor('black')
# draw a figure

ax.add_collection(fig)

# # show all of the lines to highlight ones that can not be seen
for line in verts:
	# need to add one more line 
	# connecting first and last point
	# since the side representeted with only 3 lines 
    line.append(line[0])
ax.add_collection(Line3DCollection(
    verts, colors='k', linewidths=0.2, linestyles=':'))


plt.show()
