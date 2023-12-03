import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def load_fire_data(url):
    df = pd.read_csv(url)
    return df


def visualize_fires(df):
    plt.figure(figsize=(12, 8))

    m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90, \
                llcrnrlon=-180, urcrnrlon=180, resolution='c')

    for index, row in df.iterrows():
        lon, lat = row['longitude'], row['latitude']
        brightness = row['brightness'] / 50  # Scale brightness for better visualization
        m.plot(lon, lat, 'ro', markersize=6, alpha=0.7)


    m.drawcoastlines()
    m.drawcountries()

    plt.title('Global Fire Activity (Past 24 Hours)')
    plt.show()


if __name__ == "__main__":
    url = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Global_24h.csv'

    fire_data = load_fire_data(url)

    visualize_fires(fire_data)
