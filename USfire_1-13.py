import json
import os

os.getcwd()
infile= open('US_fires_9_1-1.json', 'r')
fire_data = json.load(infile)

#extract longitude, latitude, and brightness data
bright, longitude, latitude = [],[],[]
for i in fire_data:
      if i['brightness']>450:
            longitude.append(i['longitude'])
            latitude.append(i['latitude'])
            bright.append(i['brightness'])

#check if data is loaded into lists
print(longitude[:6])
print(latitude[:6])
print(bright[:6])


from plotly.graph_objs import scattergeo, Layout
from plotly import offline 

data={'type':'scattergeo',
      'lon':longitude,
      'lat':latitude,
      'marker':{
            'size': 15,
            'color': bright,
            'colorscale': "Viridis",
            'reversescale':True,
            'colorbar':{'title':"Magnitude"}
      }}

mylayout = Layout(title='Fires in California')

fig={"data": data, 'layout':mylayout}

offline.plot(fig,filename='fires_in_california')
