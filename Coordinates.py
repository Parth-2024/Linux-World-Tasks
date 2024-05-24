import geocoder
from geopy.geocoders import Nominatim

def get_location():
    # Get your IP-based location
    g = geocoder.ip('me')
    latlng = g.latlng
    
    if not latlng:
        raise Exception("Could not get the location. Make sure you're connected to the internet.")

    latitude, longitude = latlng

    # Use geopy to get the location name
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse((latitude, longitude), exactly_one=True)

    location_name = location.address if location else "Location name not found"

    return latitude, longitude, location_name

if __name__ == "__main__":
    try:
        lat, lng, loc_name = get_location()
        print(f"Coordinates: {lat}, {lng}")
        print(f"Location Name: {loc_name}")
    except Exception as e:
        print(f"Error: {e}")
