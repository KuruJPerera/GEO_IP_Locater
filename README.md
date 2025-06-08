
# IP Geolocation Lookup in Python

This project demonstrates a simple Python script that retrieves geolocation data for a given IP address using the free [ip-api.com](http://ip-api.com) service. It uses Python’s `requests` module to make an HTTP request to the API and returns information such as the city, region, country, and ISP associated with the IP.

---

## What is IP Geolocation?

IP geolocation is the process of identifying the geographical location of an IP address. Services like `ip-api.com` estimate the location of a device based on its public IP, providing details such as:

- Country and region
- City
- Coordinates (latitude and longitude)
- Internet Service Provider (ISP)

---

## How It Works

1. The script prompts the user to enter an IP address.
2. It sends a request to the public API endpoint `http://ip-api.com/json/{IP}`.
3. The response is parsed and key data points are printed, including:
   - IP Address
   - Country
   - Region
   - City
   - Latitude and Longitude
   - ISP

If the request fails or the IP is invalid, an error message is displayed.

---

## Getting Started

### Requirements

To run this project, you’ll need:

- Python 3 installed  
- The `requests` package  
- Internet access (the API requires a network call)

If Python is not installed, download it here:  
https://www.python.org/downloads/

---

## Installation

1. Clone or download this repository  
2. Install the required module:  
   ```bash
   pip install requests
   ```

---

## Running the Program

Run the script in a terminal:

```bash
python ip_lookup.py
```

When prompted, enter an IP address (e.g., `8.8.8.8` or `213.155.225.186`).

The program will print out details about the IP's geolocation.

---

## Example Output

```
Enter an IP address: 213.155.225.186
IP Address: 213.155.225.186
Country: Sweden
Region: Stockholm
City: Stockholm
Latitude: 59.3326
Longitude: 18.0649
ISP: Bahnhof Internet AB
```
