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