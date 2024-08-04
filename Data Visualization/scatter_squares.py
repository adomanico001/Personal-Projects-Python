# Plotting and stylizing individual points
# @author Addie Domanico
# @version 05/03/2024

import matplotlib.pyplot as plt

# Calculate the data automatically
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Built-in seaborn style
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Plot a stylized point with Colormap
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# Saves plot automatically
plt.savefig('squares_plot.png', bbox_inches='tight')
