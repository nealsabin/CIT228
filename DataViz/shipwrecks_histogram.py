import json
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'DataViz/shipwrecks.json'

with open (filename, encoding="utf8") as f:
    all_ship_data = json.load(f)

all_ship_dicts = all_ship_data['features']

years_lost = []

for ship_dict in all_ship_dicts:
    try: 
        year_lost = int(ship_dict['properties']['LostYR'])
    except (ValueError,TypeError):
        print(f"Missing info.")
    else:
        years_lost.append(year_lost)

# print(years_lost)
plt.style.use('dark_background')
plt.hist(years_lost, bins=20, color='blue')
plt.ylabel("Frequency")
plt.xlabel("Year Lost")
plt.suptitle("Great Lakes Shipwrecks Year Lost")
plt.show()