import geopy
import haversine as hs
from haversine import Unit
import numpy as np

###Travelling Sales Man###
def travellingsalesman(c,neighborhoods):
    global cost
    adj_vertex = 999999
    min_val = 999999
    visited[c] = 1
    print(neighborhoods[c], end=" ")
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if min_val != 999999:
        cost = cost + min_val
    if adj_vertex == 999999:
        adj_vertex = 0
        print((neighborhoods[adj_vertex]), end=" ")
        cost = cost + tsp_g[c][adj_vertex]
        return
    travellingsalesman(adj_vertex,neighborhoods)
###Travelling Sales Man###

###Finding Latitude, Logititude from Neighborhoods###
neighborhoods = [
    "Bharathi Park",
    "Children's Park",
    "Coimbatore Municipal Park",
    "Coimbatore Managaratchi Siruvar Poonga",
    "Corporation Park",
    "Gowtham Gowtham Flora",
    "Mayflower Eden Valley",
    "Tamilnadu Ice Tovarno",
    "Trisquare Kamal",
    "Noble Imperia",
    "Majesticka Grande",
    "VRKSA Ziya",
    "Sakthi Apoorva",
    "Sakthi Subiksha",
    "Patteeswarar Heritage",
    "Ram Nagar",
    "RS Puram",
    "Tatabad",
    "Race Course",
]
API_KEY = "Ailld2CZ5cX5k1Uel13Gg4-O5VkNYasEO27CeOlgRkpjGA2cy_id26qydlvTy2Vf"  # Replace with your Bing Maps API key
geolocator = geopy.geocoders.Bing(API_KEY)
def address_to_coordinates(address):
    location = geolocator.geocode(address)
    if hasattr(location, 'latitude') and hasattr(location, 'longitude'):
        return (location.latitude, location.longitude)
    else:
        return None
addresses = []  # List of addresses to convert
for neighborhood in neighborhoods:
    location = neighborhood + ", SaibabaColony, Coimbatore, Tamilnadu"
    addresses.append(location)

coordinates = []  # List of coordinates results

for address in addresses:
    coordinate = address_to_coordinates(address)
    coordinates.append(coordinate)

###Finding Latitude, Logititude from Neighborhoods###

###Finding Distance from Latitude, Longitude###
dist_matrix = []
for i in range(len(coordinates)):
    loc1 = coordinates[i]
    dist_s = []
    for j in range(len(coordinates)):
        loc2 = coordinates[j]
        dist = hs.haversine(loc1,loc2,unit=Unit.METERS)
        dist_s.append(dist)   
    dist_matrix.append(dist_s)
###Finding Distance from Latitude, Longitude###

###Finding Shortest path###
n = len(dist_matrix)
cost = 0
visited = np.zeros(n, dtype=int)
tsp_g = np.array(dist_matrix)
print("Shortest Path:", end=" ")
travellingsalesman(0,neighborhoods)
print()
print("Minimum Cost:", end=" ")
print(cost)
###Finding Shortest path###