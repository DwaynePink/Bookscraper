import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

# Base URL for the website
base_url = "http://books.toscrape.com/catalogue/category/books_1/"