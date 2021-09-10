import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/J1_VIIRS_C2_Global_24h.csv"

brightness, lons, lats = [], [], []
with open(filename) as f:
    dataset = csv.reader(f)
    head_row = next(dataset)
    print(head_row)

    #Get Indexes
    lat_index = head_row.index('latitude')
    lon_index = head_row.index('longitude')
    brightness_index = head_row.index('bright_ti4')

    for fire in dataset:
        lats.append(fire[lat_index])
        lons.append(fire[lon_index])
        brightness.append(float(fire[brightness_index]))

print(len(brightness))
print(len(lons))
print(len(lats))

# Map the fires
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [bright/50 for bright in brightness],
        'color': 'red',
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    }
}]
my_layout = Layout(title='World on Fire')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_on_fire.html')