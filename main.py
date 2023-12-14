import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

desired_fields = ["book_title", "product_page_url", "review_rating", "category", "description", "upc", "price_excl_tax", "price_incl_tax", "availability"]

book_title_element = soup.find('h1')
book_title = book_title_element.text.strip() if book_title_element else "Unknown Title"
product_page_url = (URL)
review_rating_element = soup.find('p', class_='star-rating')
review_rating = review_rating_element['class'][1] if review_rating_element else "Unknown Rating"
category_element  = soup.find_all('ul', class_='breadcrumb')
category = category_element[0].find('a', href="../category/books/business_35/index.html").text.strip() if category_element else None
description_element = soup.find('meta', attrs={'name': 'description'})
description = description_element.get('content') if description_element else "Unknown Description"


table_data = {}
rows = soup.find_all('tr')

for row in rows:
    # Find the <th> element within the current <tr>
    header = row.find('th')

    # If <th> exists and its text is 'UPC', then proceed
    if header and header.text.strip() == 'UPC':
        # Find the corresponding <td> element
        data = row.find('td')

        # If <td> exists, extract the content
        if data:
            upc = data.text.strip()
            table_data['UPC'] = upc
        else:
            upc = "unknown"

    # If <th> exists and its text is 'Price (excl. tax)', then proceed
    if header and header.text.strip() == 'Price (excl. tax)':
        # Find the corresponding <td> element
        data = row.find('td')

        # If <td> exists, extract the content
        if data:
            price_excl_tax = data.text.strip()
            table_data['Price (excl. tax)'] = price_excl_tax
        else:
            price_excl_tax = "unknown"

    # If <th> exists and its text is 'Price (incl. tax)', then proceed
    if header and header.text.strip() == 'Price (incl. tax)':
        # Find the corresponding <td> element
        data = row.find('td')

        # If <td> exists, extract the content
        if data:
            price_incl_tax = data.text.strip()
            table_data['Price (incl. tax)'] = price_incl_tax
        else:
            price_incl_tax = "unknown"

    if header and header.text.strip() == 'Availability':
        # Find the corresponding <td> element
        data = row.find('td')

        # If <td> exists, extract the content
        if data:
            availability = data.text.strip()
            table_data['Availability'] = availability
        else:
            availability = "unknown"

img_url_element = soup.find('div', class_='item active').find('img')

if img_url_element:
    img_url = urljoin(URL, img_url_element['src'])
else:
    img_url = "Unknown Image URL"


#print(img_url_element)



#print("book_title)
#print(img_url)
# #print(product_page_url)
#print(review_rating)#
#print(category)
#print(upc)
#print(price_excl_tax)
#print(price_incl_tax)
#print(availability)
#print(description)

