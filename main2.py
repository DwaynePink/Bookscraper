import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

start_url = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# In the event there is a next page on any category this will save pages visited
urls_visited = []
