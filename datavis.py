import requests
import folium
import geopandas as gpd
from shapely.geometry import Polygon

# URL for the GeoJSON data of Gemeindebauten in Vienna
url = "https://data.wien.gv.at/daten/geo?service=WFS&request=GetFeature&version=1.1.0&typeName=ogdwien:GEMBAUTENFLOGD&srsName=EPSG:4326&outputFormat=json"

# Fetch the data
response = requests.get(url)
data = response.json()

# Convert the JSON data to a GeoDataFrame
gdf = gpd.GeoDataFrame.from_features(data['features'])

# Set the CRS to EPSG:4326
if gdf.crs is None:
    gdf.set_crs(epsg=4326, inplace=True)

# Define the bounding box for Vienna
vienna_bbox = gpd.GeoSeries(Polygon([(16.189848, 48.123497), (16.577369, 48.123497),
                                     (16.577369, 48.323742), (16.189848, 48.323742)]), crs="EPSG:4326")

# Create an interactive map centered around Vienna
m = folium.Map(location=[48.2082, 16.3738], zoom_start=12)

# Add a gray layer for the rest of the map
folium.GeoJson(
    vienna_bbox.__geo_interface__,
    style_function=lambda x: {'color': 'gray', 'weight': 1, 'fillOpacity': 0.1}
).add_to(m)

# Add the Gemeindebauten data to the map
folium.GeoJson(
    gdf,
    style_function=lambda x: {'color': 'blue', 'weight': 1, 'fillOpacity': 0.6}
).add_to(m)

# Maximize the zoom level to fit Vienna perfectly
m.fit_bounds([[48.123497, 16.189848], [48.323742, 16.577369]])

# Save the map to an HTML file
m.save("gemeindebauten_wien.html")
