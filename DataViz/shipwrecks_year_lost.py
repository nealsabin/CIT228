import json
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'DataViz/shipwrecks.json'

with open (filename, encoding="utf8") as f:
    all_ship_data = json.load(f)

all_ship_dicts = all_ship_data['features']

years_built = []

for ship_dict in all_ship_dicts:
    try: 
        year_built = int(ship_dict['properties']['Built'])
    except (ValueError,TypeError):
        print(f"Missing info.")
    else:
        years_built.append(year_built)

# print(years_lost)
plt.style.use('dark_background')
plt.hist(years_built, bins=20, color='green')
plt.ylabel("Frequency")
plt.xlabel("Year Built")
plt.suptitle("Great Lakes Shipwrecks - Ship Year Built")
plt.show()