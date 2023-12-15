import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

start_url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# In the event there is a next page on any category this will save pages visited
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

# add to function to make sure pagination
while current_url:
    current_url = extract_urls(current_url)

# Print the list of collected URLs vertically
for url in urls_visited:
    print(url)
#
