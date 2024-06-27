import requests

url = "http://api.open-notify.org/iss-now.json"


response = requests.get(url)

if response.status_code == 200:
    
    print("JSON Response:")
    print(response.json())
else:
    print(f"Error: Unable to fetch data, status code {response.status_code}")
