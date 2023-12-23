import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

# Base URL for the website
base_url = "http://books.toscrape.com/catalogue/category/books_1/"

# Create a directory to store downloaded images
image_directory = "images"
os.makedirs(image_directory, exist_ok=True)

# Function to download images from a page
def download_images(page_url):
    page = requests.get(page_url, timeout=120)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract image URLs from the page
    img_elements = soup.select('img')
    img_urls = [urljoin(page_url, img['src']) for img in img_elements]

    # Download images
    for img_url in img_urls:
        img_data = requests.get(img_url, timeout=120).content
        img_name = os.path.join(image_directory, os.path.basename(img_url))
        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)

# Iterate through all category pages
for page_number in range(1, 60):  # account for additional pages that maybe be added in the future
    category_url = f"{base_url}page-{page_number}.html"
    download_images(category_url)

