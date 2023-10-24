# Create a for loop to imput lat and lng to grab locations


import requests

def get_chicago_neighborhood(lat, lon, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
    location = f"{lat},{lon}"
    params = {
        "latlng": location,
        "result_type": "neighborhood",
        "key": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)
    print(response)
    if data["status"] == "OK":
        # Extract neighborhood information from the first result
        neighborhood = None
        for result in data["results"]:
            for address_component in result["address_components"]:
                if "neighborhood" in address_component["types"]:
                    neighborhood = address_component["long_name"]
                    break
            if neighborhood:
                break
        return neighborhood

    else:
        return None

# Replace with your Google Maps API Key
api_key = "Your_Api_Key_Here"
lat = 41.8781  # Example latitude for Chicago
lon = -87.6298  # Example longitude for Chicago

neighborhood = get_chicago_neighborhood(lat, lon, api_key)
if neighborhood:
    print(f"Neighborhood: {neighborhood}")
else:
    print("Neighborhood not found.")
