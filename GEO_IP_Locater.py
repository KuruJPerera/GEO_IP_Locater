import requests  # Import requests module

def get_ip_location(ip_address):

    try:
        url = f"http://ip-api.com/json/{ip_address}"  # Public IP Geolocation API
        
        # Store the response in a variable and parse the data from it
        response = requests.get(url)
        data = response.json()
        
        # Display relevant location details
        print(f"IP Address: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"ISP: {data['isp']}")
    
    except Exception as e:
        print(f"Error.")

# Usage
ip = input("Enter an IP address: ")
get_ip_location(ip)

# Example IP from Shodan: 213.155.225.186
