import matplotlib as mpl 
import matplotlib.pyplot as plt


# Create a plot
fig, ax = plt.subplots()

# Modify plot region
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

# Add a unit rectangle
rect = mpl.patches.Rectangle((x,y), 1, 1, facecolor='red', edgecolor='none')
ax.add_patch(rect)

# Add a line
xx = [1, 1]
yy = [1, 3]
line = mpl.lines.Line2D(xx, yy, linewidth=1, color='blue')
