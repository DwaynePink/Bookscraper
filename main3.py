import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

# Starting URL for a specific category
start_url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# List to store visited URLs- to prevent duplication of data
urls_visited = []

# Function to extract URLs from a page
def extract_urls(page_url):
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract URLs for category
    category_urls = [urljoin(page_url, link.get('href')) for link in soup.select('h3 a') if link.get('href')]
    urls_visited.extend(category_urls)

    # Check if there is a "next" link on the page
    next_page_link = soup.select_one('li.next a')
    next_page_url = urljoin(page_url, next_page_link['href']) if next_page_link else None

    return next_page_url

current_url = start_url

# Continue extracting URLs until there are no more next pages
while current_url:
    current_url = extract_urls(current_url)

# Create CSV file for saving data
csv_file_path = "book_data.csv"
fieldnames = ["book_title", "product_page_url", "review_rating", "category", "description", "upc", "price_excl_tax", "price_incl_tax", "availability", "img_url"]

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # Write the header row
    writer.writeheader()

    # Iterate over each URL and extract details
    for url in urls_visited:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        # Extract details for the individual book
        book_title_element = soup.find('h1')
        book_title = book_title_element.text.strip() if book_title_element else "Unknown Title"
        product_page_url = url
        review_rating_element = soup.find('p', class_='star-rating')
        review_rating = review_rating_element['class'][1] if review_rating_element else "Unknown Rating"
        category_element = soup.find('ul', class_='breadcrumb')
        category = category_element.find('a', href=lambda x: x and x.startswith("../category/")).text.strip() if category_element else None
        description_element = soup.find('meta', attrs={'name': 'description'})
        description = description_element.get('content') if description_element else "Unknown Description"

        table_data = {}
        rows = soup.find_all('tr')

        for row in rows:
            header = row.find('th')
            if header:
                header_text = header.text.strip()
                data = row.find('td')
                if data:
                    table_data[header_text] = data.text.strip()
                else:
                    table_data[header_text] = "Unknown"

        # Extract values from table_data
        upc = table_data.get("UPC", "Unknown")
        price_excl_tax = table_data.get("Price (excl. tax)", "Unknown")
        price_incl_tax = table_data.get("Price (incl. tax)", "Unknown")
        availability = table_data.get("Availability", "Unknown")
        img_url_element = soup.find('div', class_='item active').find('img')
        img_url = urljoin(url, img_url_element['src']) if img_url_element else "Unknown Image URL"

        # Write the data row to CSV
        writer.writerow({
            "book_title": book_title,
            "product_page_url": product_page_url,
            "review_rating": review_rating,
            "category": category,
            "description": description,
            "upc": upc,
            "price_excl_tax": price_excl_tax,
            "price_incl_tax": price_incl_tax,
            "availability": availability,
            "img_url": img_url
        })

print(f"Data has been saved to {csv_file_path}")