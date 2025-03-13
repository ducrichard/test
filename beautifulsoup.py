import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://dienmaythiennamhoa.vn/hang-tieu-dung.html'

r = requests.get(url)
soup = bs(r.content, 'html.parser')

print(soup.prettify())

product_list = []
products = soup.find_all('div', attrs={'class':'card-cate'})
for product in products:
    print(product.prettify())
    name = product.find('h3').text.strip()
    price =  product.find('p', attrs={'class':'sale-price product-sale-price'}).text.strip()
    product_list.append([name, price])

dataFrame = pd.DataFrame(product_list, columns=['Ten San Pham','Gia'])
print(dataFrame)
dataFrame.to_csv('result.csv')