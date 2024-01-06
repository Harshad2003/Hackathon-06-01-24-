import geopy

API_KEY = "Ailld2CZ5cX5k1Uel13Gg4-O5VkNYasEO27CeOlgRkpjGA2cy_id26qydlvTy2Vf"  # Replace with your Bing Maps API key

geolocator = geopy.geocoders.Bing(API_KEY)

def address_to_coordinates(address):
    location = geolocator.geocode(address)
    if hasattr(location, 'latitude') and hasattr(location, 'longitude'):
        return (location.latitude, location.longitude)
    else:
        return None

addresses = ["Parco Sempione, Milan, Italy"]  # List of addresses to convert
coordinates = []  # List of coordinates results

for address in addresses:
    coordinate = address_to_coordinates(address)
    coordinates.append(coordinate)

print(coordinates)