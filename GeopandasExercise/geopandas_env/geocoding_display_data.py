import folium
import pandas as pd

dataset = pd.read_excel("Most_visited_monuments.xlsx")

del dataset["Unnamed: 0"]

m = folium.Map(tiles = 'openstreetmap', zoom_starts = 3)

for index, row in dataset.iterrows():
    #folium.Marker([row['Lat'], row['Lon']], popup = row["Name"]).add_to(m)
    folium.Marker([row['Lat'], row['Lon']], popup ="Name: " + row["Name"] + "<br><br>" "Number of visitors: " + row["Visitors"]).add_to(m)

m.save('monuments_around_the_world.html')