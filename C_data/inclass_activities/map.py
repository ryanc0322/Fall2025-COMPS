'''
https://plotly.com/python/scatter-plots-on-maps/
https://plotly.com/python/reference/choropleth/
'''

import plotly.graph_objects as go
import pandas as pd

# Read data
df = pd.read_csv('covid.csv')

# Hover text
df['text'] = df['state'] + '<br>Positive Cases: ' + df['positive'].astype(str)

# Create choropleth map
fig = go.Figure(data=go.Choropleth(
    locations=df['state'],          
    z=df['positive'],               
    locationmode='USA-states',      
    colorscale='Reds',              
    colorbar_title='Positive Cases',
    text=df['text'],                
))

# Layout settings
fig.update_layout(
    title='COVID-19 Positive Cases by State',
    geo_scope='usa',               
)

fig.show()

