import requests
from bs4 import BeautifulSoup
import json

def get_top_restaurants(city):
    
    query = f"top restaurants in {city}".replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"

    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
       
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        
        restaurants = []
        results = soup.find_all("div", class_="VkpGBb")  

        for result in results:
            if len(restaurants) >= 10:
                break

            
            name_tag = result.find("div", class_="dbg0pd")
            name = name_tag.text if name_tag else "N/A"

           
            rating = "N/A"
            reviews = "N/A"
            address = "N/A"

            
            address_tag = result.find("div", class_="rllt__details")
            if address_tag:
                address_text = address_tag.text.strip()

                
                rating_start = address_text.find("·")
                if rating_start != -1:
                    rating_reviews = address_text[rating_start:].strip().split("·")
                    if len(rating_reviews) > 1:
                        rating = rating_reviews[0].strip()
                        reviews = rating_reviews[1].strip()

                
                address = address_text.split("·")[0].strip()

            
            restaurants.append({
                "name": name,
                "rating": rating,
                "reviews": reviews,
                "address": address
            })

        return restaurants[:10]  

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")
        return []

def save_to_json(restaurants, city):

    filename = f"restaurants_{city.lower().replace(' ', '_')}.json"
    
    restaurant_data = {r["name"]: r for r in restaurants}
    
    try:
        with open(filename, "w") as file:
            json.dump(restaurant_data, file, indent=4)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error while saving to file: {e}")

def main():
    city = input("Enter the name of a city: ")

    print(f"Fetching top restaurants in {city}...")
    restaurants = get_top_restaurants(city)

    if restaurants:
        print(f"Top {len(restaurants)} restaurants retrieved successfully!")
        save_to_json(restaurants, city)
    else:
        print("No data found. Please check your query.")

if __name__ == "__main__":
    main()