import plotly.graph_objects as go
from plotly import offline
import numpy as np

# import matplotlib.pyplot as plt  
# import numpy as np 

men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total=[36.6,44.9,37.7,24.1]
age_range=["Over 20","20-39","40-59","Over 60"]
barWidth = .25

fig = go.Figure(data=[
    go.Bar(name='Men',x=age_range, y=men),
    go.Bar(name='Women',x=age_range, y=women)
    ])

layout=fig.update_layout(
    title='Fast Food Consumption',
    title_font_size=28
)

# fig.update_layout(barmode='group')
# fig.show() 
offline.plot({'data': fig, 'layout':layout}, filename='Chapter15/chart.html')