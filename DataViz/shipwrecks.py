import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'DataViz/shipwrecks.json'
with open (filename, encoding="utf8") as f:
    all_ship_data = json.load(f)

all_ship_dicts = all_ship_data['features']

depths, lons, lats, hover_texts = [], [], [], []

for ship_dict in all_ship_dicts:
    try: 
        depth = int(ship_dict['properties']['Depth'])
        lon = ship_dict['geometry']['coordinates'][0]
        lat = ship_dict['geometry']['coordinates'][1]
        title = ship_dict['properties']['Vessel']
    except TypeError:
        print(f"{title} missing depth info.")
    else: 
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(title)
        depths.append(depth)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [int(depth)/5 for depth in depths],
        'color': depths,
        'colorscale': 'Reds',
        'colorbar': {'title': 'Resting Depth'},
    }
}]

my_layout = Layout(
    title='Shipwrecks of the Great Lakes',
    geo = dict(
            showframe = True,
            framecolor = "rgb(82, 82, 82)",
            framewidth = 2,
            scope='usa',
            showland = True,
            showlakes = True,
            showrivers = True,
            lakecolor = "rgb(148, 195, 234)",
            rivercolor = "rgb(40, 110, 168)",
            landcolor = "rgb(145, 195, 138)",
            resolution = 50,
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5,
            center=dict(
                lon = -86.59149,
                lat = 44.10808,
            ),
            projection=dict(
                scale = 2,
            ),
        ),
    )

fig = {'data': data, 'layout':my_layout}
offline.plot(fig, filename='DataViz/index.html')

# readable_file = 'DataViz/shipwrecks.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_ship_data, f, indent=4)
