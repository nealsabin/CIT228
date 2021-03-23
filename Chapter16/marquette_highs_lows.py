import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'Chapter16/marquetteHighLow.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else: 
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily high and low temperatures, 1/1/2021 to 3/20/21", fontsize=18)
ax.set_xlabel('', fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
