import json

from collections import Counter

import matplotlib.pyplot as plt

filename = 'DataViz/shipwrecks.json'

with open (filename, encoding="utf8") as f:
    all_ship_data = json.load(f)

all_ship_dicts = all_ship_data['features']

lakes_lost = []

for ship_dict in all_ship_dicts:
    try: 
        lake_lost = ship_dict['properties']['Lake']
    except (ValueError,TypeError):
        print(f"Missing info.")
    else:
        lakes_lost.append(lake_lost)

superior_count = lakes_lost.count("Superior")
michigan_count = lakes_lost.count("Michigan")
huron_count = lakes_lost.count("Huron")
ontario_count = lakes_lost.count("Ontario")
erie_count = lakes_lost.count("Erie")

# print(superior_count)
# print(michigan_count)
# print(huron_count)
# print(ontario_count)
# print(erie_count)

labels = 'Superior', 'Michigan', 'Huron'
lake_count = [superior_count, michigan_count, huron_count]

plt.style.use('dark_background')
explode = (.05,.05,.05)
wedgeColors = ('red','green','blue')
fig1, ax1 = plt.subplots()
ax1.pie(lake_count, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=45, colors=wedgeColors)
ax1.axis('equal')
plt.suptitle('Ships Lost By Lake')

plt.show()
