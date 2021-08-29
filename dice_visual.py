from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two d6 dice
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll in range(50_000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
range_of_results = range(2, max_result+1)
frequencies = [results.count(value) for value in range_of_results]


# Visualize the results.
x_values = list(range_of_results)
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 50_000 times.',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')