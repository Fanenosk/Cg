import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.colors import LightSource

fig = plt.figure(1)    
ax = fig.add_subplot(111, projection='3d')

print("Please enter accuracy of approximation \n(how many rect at the slice of sphere) default 20:")
approx = int(input())

print("Enter the power of ligth source 0 < k < 1")

k = float(input())

frac = k

u = np.linspace(0, 2 * np.pi, approx)

v = np.linspace(0, np.pi, approx)

X = np.outer(np.cos(u), np.sin(v))

Y = np.outer(np.sin(u), np.sin(v))

Z = np.outer(np.ones(np.size(u)), np.cos(v))

light = LightSource(azdeg=0, altdeg=60) 

rgb = np.ones((X.shape[0], X.shape[1], 3))

illuminated_surface = light.shade_rgb(rgb, X, fraction=frac)

ax.plot_surface(X,Y,Z, linewidth=0.0, facecolors=illuminated_surface, shade = False)

ax.set_aspect('equal')

plt.show()