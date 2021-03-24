import json

import matplotlib.pyplot as plt
from numpy.random import random
from matplotlib import cm 

filename = 'DataViz/shipwrecks.json'
with open (filename, encoding="utf8") as f:
    all_ship_data = json.load(f)

all_ship_dicts = all_ship_data['features']

depths, ship_lengths = [], []

for ship_dict in all_ship_dicts:
    try: 
        depth = int(ship_dict['properties']['Depth'])
        ship_length = int(ship_dict['properties']['Length'])
    except (TypeError, ValueError):
        print(f"Missing depth or ship length info.")
    else: 
        depths.append(depth)
        ship_lengths.append(ship_length)

plt.style.use('dark_background')
initial_cmap = cm.get_cmap('Wistia')
# reversed_cmap=initial_cmap.reversed()

ax=plt.subplot()
ax.scatter(depths, ship_lengths, c=ship_lengths, cmap=initial_cmap, s=75, label="Ship Retrieval Difficulty")

plt.ylabel('Ship Length (ft)')
plt.xlabel('Resting Depth (ft)')
plt.title('Ship Length - Ship Resting Depth')
plt.suptitle('Ship Retrieval Difficulty')

plt.grid()
plt.show()
