from bs4 import BeautifulSoup
import requests

try:
    req = requests.get("https://helloomarket.com/")
    req.raise_for_status
    
    soup = BeautifulSoup(req.content, "html.parser")
    
    products = soup.find('div', class_="box-product").findAll('div', class_="product-items")
    for product in products:
        product_name = product.find('div', class_="product-details").a.text
        product_link = product.find('div', class_="product-details").a.get("href")
        product_price = product.find('div', class_="product-details").p.get_text(strip=True)
        
        print(product_price)
        break
      
except Exception as e:
    print(e)