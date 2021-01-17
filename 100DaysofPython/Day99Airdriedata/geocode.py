from googlemaps import Client as GoogleMaps
import os
import pandas as pd
import time


# Load ENV variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
GOOGLE_MAPS_KEY = os.getenv('GOOGLE_MAPS_KEY')

gmaps = GoogleMaps(key=GOOGLE_MAPS_KEY)

# create dataframe from csv file
df = pd.read_csv(
    '/Users/smith/python/100DaysofPython/Day99Airdriedata/airdrie_props.csv')

# Create list of addressedsfrom dataframe
addresses = [address for address in df['address']]


i = 0  # counter

# Geocode addresses
for address in addresses[0:]:
    # initialize variable
    row = {
        'address': address,
        'lat': 'n/a',
        'lon': 'n/a',
    }
    try:
        time.sleep(0.2)  # to add delay in case of large DFs
        print(i)
        geocode_result = gmaps.geocode(f"{address}, Airdrie, AB")
        row['lat'] = geocode_result[0]['geometry']['location']['lat']
        row['lon'] = geocode_result[0]['geometry']['location']['lng']
    except IndexError:
        print("Address was wrong...")
    except Exception as e:
        print("Unexpected error occurred.", e)

    with open("/Users/smith/python/100DaysofPython/Day99Airdriedata/airdrie_props_geocode.csv", mode="a") as file:
        file.write(f"{row['address']},{row['lat']},{row['lon']}\n")
    i += 1
