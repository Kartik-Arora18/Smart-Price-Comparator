import requests 
from bs4 import BeautifulSoup
def find_price(URL):
    try:
        r = requests.get(URL, headers={"User-Agent": "Defined"})
        soup = BeautifulSoup(r.content, "html.parser")
        if 'nykaa' in URL:
            price = soup.find(class_="css-u05rr")
            return price.text.strip() if price else None
        
        
        elif 'flipkart' in URL:
            price = soup.find(class_='_30jeq3 _16Jk6d')
            return price.text.strip() if price else None
    except Exception:
        return None

URL1 = input("Enter the first link of the item: ")
price1 = find_price(URL1)
URL2 = input("Enter the second link of the item: ")
price2 = find_price(URL2)
# URL3 = input("Enter the third link of the item:")
# price3= find_price(URL3)
# print(price3)
if price1 is None:
    print("Invalid Link or Price not found")
else:
    print(f"Price: {price1}")

if price2 is None:
    print("Invalid Link or Price not found")
else:
    print(f"Price: {price2}")

if(price1<price2):
        print("Nykaa Price is cheap")
elif(price1 == price2):
        print("Equal prices")
else:
        print("Flipkart price is cheap")