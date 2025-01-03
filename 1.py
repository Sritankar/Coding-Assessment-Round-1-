# Importing necessary libraries
import requests  # For sending HTTP requests
from bs4 import BeautifulSoup  # For parsing the HTML response
import json  # For handling JSON data storage

# Function to fetch top restaurants data
def get_top_restaurants(city):
    # Constructing the search query for the Google search URL by replacing spaces with "+" in the city name
    query = f"top restaurants in {city}".replace(" ", "+")
    # Creating the URL with the search query
    url = f"https://www.google.com/search?q={query}"

    # Setting headers to simulate a browser request (User-Agent to avoid being blocked by Google)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Sending the HTTP GET request to Google search with headers
        response = requests.get(url, headers=headers)
        # Checking if the response status is OK (status code 200)
        response.raise_for_status()
        # Parsing the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # List to store restaurant data
        restaurants = []
        # Finding all elements on the page that match the class 'VkpGBb' (restaurant entries)
        results = soup.find_all("div", class_="VkpGBb")

        # Looping through the found restaurant entries
        for result in results:
            # Limiting the number of restaurants to 10
            if len(restaurants) >= 10:
                break

            # Extracting the name of the restaurant (if present)
            name_tag = result.find("div", class_="dbg0pd")
            name = name_tag.text if name_tag else "N/A"

            # Initializing variables for rating, reviews, and address
            rating = "N/A"
            reviews = "N/A"
            address = "N/A"

            # Finding and extracting the address and additional details
            address_tag = result.find("div", class_="rllt__details")
            if address_tag:
                address_text = address_tag.text.strip()

                # Finding the separator '·' and splitting the address text into rating and reviews
                rating_start = address_text.find("·")
                if rating_start != -1:
                    rating_reviews = address_text[rating_start:].strip().split("·")
                    if len(rating_reviews) > 1:
                        rating = rating_reviews[0].strip()  # Extracting rating
                        reviews = rating_reviews[1].strip()  # Extracting reviews

                # Extracting the address
                address = address_text.split("·")[0].strip()

            # Storing the restaurant details in a dictionary and appending to the list
            restaurants.append({
                "name": name,
                "rating": rating,
                "reviews": reviews,
                "address": address
            })

        # Returning only the top 10 restaurants
        return restaurants[:10]

    # Handling any request exceptions
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")
        return []

# Function to save the restaurant data to a JSON file
def save_to_json(restaurants, city):
    # Creating the filename based on the city name, replacing spaces with underscores
    filename = f"restaurants_{city.lower().replace(' ', '_')}.json"
    
    # Creating a dictionary from the restaurant list, using the restaurant names as keys
    restaurant_data = {r["name"]: r for r in restaurants}

    try:
        # Opening the file in write mode and dumping the restaurant data as JSON
        with open(filename, "w") as file:
            json.dump(restaurant_data, file, indent=4)
        print(f"Data saved to {filename}")
    except IOError as e:
        # Handling file I/O exceptions
        print(f"Error while saving to file: {e}")

# Main function to control the flow
def main():
    # Asking the user to input a city name
    city = input("Enter the name of a city: ")

    # Informing the user that the data is being fetched
    print(f"Fetching top restaurants in {city}...")
    
    # Fetching the top restaurant data for the given city
    restaurants = get_top_restaurants(city)

    # If restaurants were successfully fetched, save the data to JSON
    if restaurants:
        print(f"Top {len(restaurants)} restaurants retrieved successfully!")
        save_to_json(restaurants, city)
    else:
        # If no data was found, print an error message
        print("No data found. Please check your query.")

# This block ensures that the main function runs when the script is executed
if __name__ == "__main__":
    main()
