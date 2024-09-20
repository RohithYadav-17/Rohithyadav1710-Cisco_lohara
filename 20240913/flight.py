import requests

# Your API key (keep this secure and do not share it publicly)
api_key = '9489a6ebb85b9b7c89bbc37f8cdf399c'

# Base URL for the Aviation Stack API
base_url = 'http://api.aviationstack.com/v1/'

# Example endpoint (e.g., flights)
endpoint = 'flights'

# Predefined dictionary mapping city names to IATA airport codes
city_to_iata = {
    'Bengaluru': 'BLR',
    'Hyderabad': 'HYD',
    'New York': 'JFK',
    'Los Angeles': 'LAX',
    # Add more cities and their corresponding IATA codes as needed
}

# Get custom input from the user
source_city = input("Enter the source city: ")
destination_city = input("Enter the destination city: ")

# Convert city names to IATA codes
source_iata = city_to_iata.get(source_city)
destination_iata = city_to_iata.get(destination_city)

# Check if the city names are valid
if not source_iata or not destination_iata:
    print("Invalid city name(s). Please check your input.")
else:
    # Parameters for the request
    params = {
        'access_key': api_key,
        'dep_iata': source_iata,  # Source airport code
        'arr_iata': destination_iata,  # Destination airport code
        'limit': 10  # Example parameter to limit the number of results
    }

    # Make the request
    response = requests.get(base_url + endpoint, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")
