import plotly.express as px

from random_walk import RandomWalk


# Make a random walk.
rw = RandomWalk(50_000)
rw.fill_walk()

# Plot the points in the walk.
df = px.data.iris()
num_of_plots = range(50000)
fig = px.scatter(df, x=rw.x_values, y=rw.y_values, color=num_of_plots)
fig.show()

