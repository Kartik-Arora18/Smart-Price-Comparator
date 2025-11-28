# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def fetch_product_price_flipkart(product_name):
#     # Initialize Chrome WebDriver
#     driver = webdriver.Chrome()  # Make sure Chrome WebDriver is installed and in PATH

#     try:
#         # Open the Flipkart website
#         driver.get("https://www.flipkart.com")

#         # Wait for the search box to be visible
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))

#         # Find the search box and enter the product name
#         search_box = driver.find_element_by_name("q")
#         search_box.send_keys(product_name)
#         search_box.submit()

#         # Wait for the search results container to be visible
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "_1AtVbE")))

#         # Find the first search result (assuming it's the desired product)
#         first_result = driver.find_element_by_xpath("//div[@class='_1AtVbE']")

#         # Extract the product title and price
#         product_title = first_result.find_element_by_xpath(".//a").text
#         product_price = first_result.find_element_by_class_name("_30jeq3").text

#         return product_title, product_price
#     finally:
#         # Close the browser window
#         driver.quit()

# def fetch_product_price_amazon(product_name):
#     # Initialize Chrome WebDriver
#     driver = webdriver.Chrome()  # Make sure Chrome WebDriver is installed and in PATH

#     try:
#         # Open the Amazon website
#         driver.get("https://www.amazon.com")

#         # Wait for the search box to be visible
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))

#         # Find the search box and enter the product name
#         search_box = driver.find_element_by_id("twotabsearchtextbox")
#         search_box.send_keys(product_name)
#         search_box.submit()

#         # Wait for the search results container to be visible
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "s-result-list")))

#         # Find the first search result (assuming it's the desired product)
#         first_result = driver.find_element_by_xpath("//div[@class='s-result-item']")

#         # Extract the product title and price
#         product_title = first_result.find_element_by_xpath(".//h2").text
#         product_price = first_result.find_element_by_class_name("a-price").text

#         return product_title, product_price
#     finally:
#         # Close the browser window
#         driver.quit()

# # Example usage
# product_name = input("Enter the product name: ")
# flipkart_result = fetch_product_price_flipkart(product_name)
# amazon_result = fetch_product_price_amazon(product_name)

# if flipkart_result:
#     flipkart_title, flipkart_price = flipkart_result
#     print("Flipkart:")
#     print(f"Title: {flipkart_title}")
#     print(f"Price: {flipkart_price}")
# else:
#     print("Product not found on Flipkart or price not available.")

# if amazon_result:
#     amazon_title, amazon_price = amazon_result
#     print("\nAmazon:")
#     print(f"Title: {amazon_title}")
#     print(f"Price: {amazon_price}")
# else:
#     print("Product not found on Amazon or price not available.")

# # Comparing prices
# if flipkart_result and amazon_result:
#     flipkart_price_num = float(flipkart_price.replace('₹', '').replace(',', ''))
#     amazon_price_num = float(amazon_price.replace('$', '').replace(',', ''))

#     if flipkart_price_num < amazon_price_num:
#         print("\nFlipkart is cheaper.")
#     elif flipkart_price_num > amazon_price_num:
#         print("\nAmazon is cheaper.")
#     else:
#         print("\nBoth Amazon and Flipkart offer the same price.")

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options) 
wait = WebDriverWait(driver, 10)

def extract_product_data(product_div):
    product_data = {}
    product_data['name'] = product_div.find_element(By.CLASS_NAME, 'KzDlHZ').text
    product_data['rating'] = product_div.find_element(By.CLASS_NAME, 'XQDdHH').text
    product_data['ratings_and_reviews'] = product_div.find_element(By.CLASS_NAME, 'Wphh3N').text
    product_data['features'] = [li.text for li in product_div.find_elements(By.XPATH, ".//ul[@class='G4BRas']/li")]
    product_data['discounted_price'] = product_div.find_element(By.CLASS_NAME, 'Nx9bqj').text
    original_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".yRaY8j"))
)
    product_data['original_price'] = original_element.text
    discount_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'UkUFwK')))
    product_data['discount'] = discount_element.text
    return product_data

def extract_page_data():
    product_divs = driver.find_elements(By.XPATH, "//div[@class='_75nlfW']")
    all_product_data = []
    for product_div in product_divs:
        product_data = extract_product_data(product_div)
        all_product_data.append(product_data)
        print_product_data(product_data)
    return all_product_data

def print_product_data(product_data):
    print("Name:", product_data['name'])
    print("Rating:", product_data['rating'])
    print("Ratings and Reviews:", product_data['ratings_and_reviews'])
    print("Features:")
    for feature in product_data['features']:
        print("- ", feature)
    print("Discounted Price:", product_data['discounted_price'])
    print("Original Price:", product_data['original_price'])
    print("Discount:", product_data['discount'])
    print()

base_url = "https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy%2C4io&page="

for page_num in range(1, 11):
    url = base_url + str(page_num)
    driver.get(url)
    time.sleep(10)  
    print(f"Scraped data from page {page_num}")
    extract_page_data()

# Close the WebDriver
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_amazon_page(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    product_divs = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

    for product_div in product_divs:
        try:
            product_title_element = product_div.find_element(By.XPATH, './/h2/a/span')
            product_title = product_title_element.text
            print("Product Title:", product_title)

            price_element = product_div.find_element(By.XPATH, './/span[@class="a-price"]')
            price = price_element.text
            print("Price:", price)

        except Exception as e:
            print("Error occurred:", str(e))

    driver.quit()

num_pages = 5  

# Scrape each page
for page_num in range(1, num_pages + 1):
    url = f"https://www.amazon.in/s?k=iphone&qid=1713807378&ref=sr_pg_{page_num}"
    print("Scraping page:", page_num)
    scrape_amazon_page(url)
    time.sleep(2)