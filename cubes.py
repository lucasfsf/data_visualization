import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=5)

# Set chart title and label axes
ax.set_title("Cubes", fontsize=20)
ax.set_xlabel("Original Values", fontsize=20)
ax.set_ylabel("Cubed Number", fontsize=12)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=12)

# Set the range of each axis
ax.axis([0, 5500, 0, 126000000000])
plt.show()