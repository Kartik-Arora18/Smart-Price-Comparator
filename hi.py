import requests 
from bs4 import BeautifulSoup

def find_price(URL):
    r = requests(URL,headers = {"User-Agent":"Defined"})
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        if 'amazon' in URL:
            price = soup.find(id = 'a-price-whole')
            return price    

        elif 'flipkart' in URL:
            price = soup.find(class_ = '_30jeq3 _16Jk6d')
            return price
    except:
        return        

URL = input("Enter the link of the item ::")
price = find_price(URL)
if price == None:
    print("Invalid Link")
else:
    print(price.get_text())