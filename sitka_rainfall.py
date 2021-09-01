
from datetime import datetime

import matplotlib.pyplot as plt

import csv

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Getting index of PRCP and DATE
    date_index = header_row.index("DATE")
    precipitation_index = header_row.index("PRCP")
    station_name_index = header_row.index("NAME")

    # Create a variable to store the station name from the fisrt row in data
    station_name = None
    
    # Get dates, and high and low temperatures from this file.
    dates, rains = [], []
    for row in reader:
        if station_name == None:
            station_name = row[station_name_index]
        try:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            current_rain = float(row[precipitation_index])
        except ValueError:
            print(f"Missing value at {current_date}")
        else:
            dates.append(current_date)
            rains.append(current_rain)

# Plot the dates and rain for 2018 in Sitka
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='blue')

# Format Plot
ax.set_title(f"Precipitation 2018 - \n {station_name} ", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()