import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys, os

sys.path.append(os.path.realpath('..'))

# Read the CSV file into a DataFrame
df = pd.read_csv('csv/data.csv', header=None, names=['x', 'y', 'z'])

# Create a 2D grid of values with increased precision
x = np.linspace(df['x'].min(), df['x'].max(), 100)
y = np.linspace(df['y'].min(), df['y'].max(), 100)
X, Y = np.meshgrid(x, y)

# Interpolate the z-values onto the new grid
from scipy.interpolate import griddata

Z = griddata((df['x'], df['y']), df['z'], (X, Y), method='cubic')

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
fig.colorbar(surf, shrink=0.5, aspect=5)

# Set the axis labels
ax.set_xlabel('R')
ax.set_ylabel('PHI')
ax.set_zlabel('E')

if os.path.exists('plot/plot.pdf'):
    os.remove('plot/plot.pdf')
if os.path.exists('plot/plot.png'):
    os.remove('plot/plot.png')

# Plotting curve in xy-plane
plt.plot(x, y, "k", zorder = 3)

# Save the plot in PDF and PNG
plt.savefig('plot/plot.pdf', dpi=300, bbox_inches='tight')
plt.savefig('plot/plot.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()