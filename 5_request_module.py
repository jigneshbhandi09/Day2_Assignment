import requests
import json


url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Extract latitude, longitude, and timestamp
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']
    
    # Print the extracted data
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Timestamp:", timestamp)
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
