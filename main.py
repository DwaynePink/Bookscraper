import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

desired_fields = ["book_title", "product_page_url", "review_rating", "category",]

book_title_element = soup.find('h1')
book_title = book_title_element.text.strip() if book_title_element else "Unknown Title"
product_page_url = (URL)
review_rating_element = soup.find('p', class_='star-rating')
review_rating = review_rating_element['class'][1] if review_rating_element else None
category_element  = soup.find_all('ul', class_='breadcrumb')
category = category_element[0].find('a', href="../category/books/business_35/index.html").text.strip() if category_element else None
description_element = soup.find('meta', attrs={'name': 'description'})
description = description_element.get('content') if description_element else None


#description = soup.find('article', class_=('product_page'))







#print(book_title)
#print(product_page_url)
#print(review_rating)
#print(category)
#print(description)





#image file contained in here
#description = soup.find('article', class_=('product_page'))


