import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline
import plotly.express as px

infile = open("US_fires_9_14.json", "r")

Fire_data = json.load(infile)

Bright_Fires = [fire for fire in Fire_data if fire["brightness"] >= 450]

brightnesses, lats, lons = [], [], []

for fire in Bright_Fires:
    brightnesses.append(fire["brightness"])
    lons.append(fire["longitude"])
    lats.append(fire["latitude"])

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [0.035 * brightness for brightness in brightnesses],
            "color": brightnesses,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

Graph_legend = {"title": "Brightness"}

my_layout = Layout(
    title="US Fires - 9/14/2020 through 9/20/2020",
    legend=Graph_legend,
)
fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="California_Fires.html")
