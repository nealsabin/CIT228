import matplotlib.pyplot as plt

labels = 'PNG','JPEG','SVG','GIF','Other'
usage = [376,348,153,104,19]
explode = (.1,0,0,0,0)
wedgeColors = ('red','green','blue','orange','purple')
fig1, ax1 = plt.subplots()
ax1.pie(usage, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=45, colors=wedgeColors)
ax1.axis('equal')
plt.suptitle('Most Popular Image Types')

plt.show()