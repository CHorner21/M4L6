import requests
import matplotlib.pyplot as plt
from datetime import datetime
from mpl_toolkits.basemap import Basemap


def download_earthquake_data(url):
    response = requests.get(url)
    data = response.json()
    return data


def visualize_earthquakes(data):
    plt.figure(figsize=(12, 8))

    m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90, \
                llcrnrlon=-180, urcrnrlon=180, resolution='c')

    for feature in data['features']:
        coords = feature['geometry']['coordinates']
        lon, lat = coords[:2]
        m.plot(lon, lat, 'ro', markersize=6, alpha=0.7, color='b')

    m.drawcoastlines()
    m.drawcountries()

    plt.title('Recent Earthquake Activity')
    plt.show()


if __name__ == "__main__":
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'

    earthquake_data = download_earthquake_data(url)

    visualize_earthquakes(earthquake_data)
