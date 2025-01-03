Top Restaurants Scraper
This Python script scrapes the top restaurants in a given city from Google search results and saves the details to a JSON file.

Prerequisites
Before running the script, make sure you have the following:

Python 3.x
requests library
beautifulsoup4 library
You can install the required libraries by running the following command:


pip install requests beautifulsoup4
Script Overview
This script:

Accepts a city name as input.
Performs a Google search to find the top restaurants in the city.
Scrapes the restaurant names, ratings, reviews, and addresses from the search results.
Saves the scraped restaurant information into a JSON file, named restaurants_<city>.json.
How to Run
Download the script: Save the script as 1.py.

Run the script:

Open a terminal or command prompt, navigate to the directory where the script is located, and run:


python 1.py
Enter the city name when prompted:

You'll be asked to enter the name of the city for which you want to scrape the top  restaurants. For example, type Bangalore.

Check the output:

After the script finishes scraping, it will create a JSON file with the name restaurants_<city>.json. The file will contain the details of the top 10 restaurants.

Example
For example, when running the script for the city Bangalore, you will get a JSON file named restaurants_bangalore.json with the following structure:


{
    "Restaurant 1": {
        "name": "Restaurant 1",
        "rating": "4.5",
        "reviews": "1000",
        "address": "Address of Restaurant 1"
    },
    "Restaurant 2": {
        "name": "Restaurant 2",
        "rating": "4.2",
        "reviews": "800",
        "address": "Address of Restaurant 2"
    },
    ...
}
Notes
This script is designed to work with Google search results. As Google search results can change their structure, the script may break if the HTML structure of the results page changes. In such cases, you might need to inspect the page and update the scraping logic accordingly.
The script retrieves a maximum of 10 restaurants. You can modify the script to scrape more if needed by changing the if len(restaurants) >= 10 condition.
Error Handling
If there is an issue with fetching data (e.g., due to a network error or bad request), the script will print an error message, and no data will be saved.

Difficuilty faced while writing the code

While working on the restaurant data scraping, I faced a few challenges. Google’s search results are dynamic, and many details like ratings, reviews, and addresses are rendered via JavaScript, which our current scraping method can’t access. Additionally, some restaurant information is incomplete, and we may run into issues with rate-limiting or blocking from Google due to frequent requests. The HTML structure of the page also changes often, making it difficult to consistently extract the required data. I recommend using the Google Places API for more reliable and structured data.



