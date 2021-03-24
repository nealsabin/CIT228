import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'DataViz/surface_temps.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    days, superior_temps, michigan_temps, huron_temps, erie_temps, ontario_temps  = [],[],[],[],[],[]
    for row in reader:
        day = int(row[1])
        try:             
            superior_temp = float(row[2])
            michigan_temp = float(row[3])
            huron_temp = float(row[4])
            erie_temp = float(row[5])
            ontario_temp = float(row[6])
        except ValueError:
            print(f"Missing info.")
        else:
            days.append(day)
            superior_temps.append(superior_temp)
            michigan_temps.append(michigan_temp)
            huron_temps.append(huron_temp)
            erie_temps.append(erie_temp)
            ontario_temps.append(ontario_temp)

plt.style.use('seaborn')
plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.plot(days, superior_temps, c='blue', label="Superior")
ax.plot(days, michigan_temps, c='yellow', label="Michigan")
ax.plot(days, huron_temps, c='green', label="Huron")
ax.plot(days, erie_temps, c='purple', label="Erie")
ax.plot(days, ontario_temps, c='red', label="Ontario")

ax.set_title("Average Lake Surface Temp By Day", fontsize=14)
ax.set_xlabel('Days - 1/1/2020 to 12/31/2020', fontsize=14)
ax.set_ylabel("Temperature (C)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=14)

plt.legend(loc="upper left")
plt.show()