import requests
from lxml import html
import pandas as pd
import os
import csv

# URL of the restaurant

file_path = 'restaurants.csv'
subpage_file_path = 'subpage.csv'
df = pd.read_csv(file_path)

urls = df.iloc[:, 6].dropna().tolist()

if not os.path.exists(subpage_file_path):
    pd.DataFrame().to_csv(subpage_file_path, index=False)

headers = ['Opening Hours', 'Popular Dishes', 'Detailed Address']

with open(subpage_file_path, 'w', newline='', encoding='utf-8', errors='ignore') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    if os.stat(subpage_file_path).st_size == 0:
        writer.writeheader()
    for url in urls:
        print(url)

        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content
        tree = html.fromstring(response.content)

        # Data to be stored in CSV
        data = []

        table_xpath = '//*[@id="location-and-hours"]/section/div[2]/div[2]/div/div/table/tbody'

        # Extract the table element
        table = tree.xpath(table_xpath)

        # List to hold opening hours
        open_hours = []

        # Iterate through each row (tr) inside the table
        # Iterate through each row (tr) inside the table, starting from the second row
        if table:
            rows = table[0].xpath('.//tr')[1:]  # Skip the first row if it's a header
            for row in rows:
                day_elements = row.xpath('.//th/p/text()')
                hours_elements = row.xpath('.//td[1]/ul/li/p/text()')
                if day_elements and hours_elements:
                    day = day_elements[0].strip()
                    hours = " ".join(hours_elements).strip()  # Joining hours if they are in multiple elements
                    open_hours.append(f"{day}: {hours}")

        # Print the opening hours
        for hours in open_hours:
            print(hours)

        # Generalized XPath to match all the popular dishes
        dishes_xpath = '//*[@id="main-content"]/section[1]/div[3]/div/div/div/div/div[*]/div/div/a/div/div[2]/div/div/p'

        # Find all the dish elements
        dishes_elements = tree.xpath(dishes_xpath)

        # List to hold popular dishes
        popular_dishes = [dish.text_content().strip() for dish in dishes_elements]

        # Print the popular dishes
        for dish in popular_dishes:
            print(dish)

        # XPath to the address element
        address_xpath = '//*[@id="location-and-hours"]/section/div[2]/div[1]/div/div/div/div[1]/address'

        # Extract the address element
        address_elements = tree.xpath(address_xpath)

        # Check if the address was found
        if address_elements:
            address = address_elements[0].text_content().strip()
        else:
            address = 'Not Found'

        # Print the address
        print(address)

        data = {
            'Opening Hours': open_hours,
            'Popular Dishes': popular_dishes,
            'Detailed Address': address,
        }
        writer.writerow(data)
        print("CSV file has been saved.")
