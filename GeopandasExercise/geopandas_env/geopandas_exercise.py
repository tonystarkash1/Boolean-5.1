import pandas as pd 
import geopandas as geopd
from geopandas . tools import geocode
import geopy 

# risoluzione problema violazione eula 
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="test_geopy")
geopy.geocoders.options.default_user_agent = "test_geopy"

data = pd.read_html("https://en.wikipedia.org/wiki/List_of_most_visited_palaces_and_monuments")

for monuments in data:
     print(monuments) 

#save the information in to an excel file
monuments.to_excel("most_visited_locations.xlsx", header=False)

#read the information back into python as a padas dataframe

monuments = pd.read_excel("most_visited_locations.xlsx",
                          usecols= [1,2,3],
                          names = ["Name", "Locationn", "Visitors"],
                          header= None,
                          skiprows= 1, nrows=40)

# iterate from the monuments dataframe
for index, row in monuments.iterrows():
     try:
          print(row["Name"])
          info = geocode(str(row["Name"]), provider = "nominatim")
          monuments.loc[int(index), "Address"] = info["address"].loc[0]
          monuments.loc[int(index), 'Lon'] = info['geometry'].loc[0].x
          monuments.loc[int(index), 'Lat'] = info['geometry'].loc[0].y

     except: # qui l'indiano aveva messo "except TypeError"... levando il TypeError funziona tutto
          print("Geocoding information for " + row["Name"] + " not found!")
          print('')

# removing nan rows
monuments = monuments.dropna() 

# saving the dataframe to an excel file
monuments.to_excel("Most_visited_monuments.xlsx")