import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

desired_fields = ["book_title", "product_page_url", "review_rating", "category",]

book_title = soup.find('h1')
product_page_url = (URL)
review_rating_element = soup.find('p', class_='star-rating')
review_rating = review_rating_element['class'][1] if review_rating_element else None


print(book_title)
print(product_page_url)
print(review_rating)



c = soup.find_all(lambda tag: tag.name == 'a' and '../category/books/poetry_23' in tag.get('href', ''))





print



#review_rating = soup.find('p', class_= "star-rating Four").

#print(book_title)
#print(product_page_url)

