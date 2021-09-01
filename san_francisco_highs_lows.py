import csv
from datetime import datetime
from os import stat

import matplotlib.pyplot as plt

filename = 'data/san_francisco.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Getting index of TMAX, TMIN and DATE
    tmax_index = header_row.index("TMAX")
    tmin_index = header_row.index("TMIN")
    date_index = header_row.index("DATE")
    station_name_index = header_row.index("NAME")

    # Create a variable to store the station name from the fisrt row in data
    station_name = None
    
    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        if station_name == None:
            station_name = row[station_name_index]
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[tmax_index])
            low = int(row[tmin_index])
        except ValueError:
            print(f"Missing date for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
    print(station_name)

# Plot the high and temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title(f"Daily high and low temperatures 2018 - \n {station_name} ", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.set_ylim([20,140])
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()