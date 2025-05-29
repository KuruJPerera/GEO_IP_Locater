What is IP Geolocation?

IP Geolocation is the process of determining the geographic location of a device based on its IP address. Services like ip-api.com make this possible by mapping IP ranges to physical locations.

This script shows how to access that data using Python’s requests module and basic JSON parsing.

How It Works:

The script does the following:

. Prompts the user to enter an IP address

. Sends a request to http://ip-api.com/json/<IP>

. Parses the returned JSON response

Displays the following location information:

. IP Address

. Country

. Region

. City

. Latitude and Longitude

. ISP

Getting Started: Requirements:

To run this project, you’ll need:

. Python 3 installed on your computer

. A basic code editor or IDE

. An internet connection (to access the API)

. The requests library (install it using pip install requests if needed)

If you don’t already have Python, you can download it here:
https://www.python.org/downloads/

Installation:

Download or clone this repository to your local machine

Open the script in your preferred code editor

Running the Program:

. Run the Python script

. When prompted, enter a valid IP address (e.g. 8.8.8.8)

. The program will display the location details directly in the terminal
