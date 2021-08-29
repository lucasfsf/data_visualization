import matplotlib.pyplot as plt

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
print(frequencies)

# Visualize the results as a bar graph
plt.bar(list(range_of_results), frequencies, color='blue')

plt.xlabel('Results')
plt.ylabel('Probability')
plt.title('Results of trowing a D6 and a D10 50.000 times')
plt.xlim(2, max_result)
plt.ylim(0, 6000)
plt.grid(False)
plt.show()