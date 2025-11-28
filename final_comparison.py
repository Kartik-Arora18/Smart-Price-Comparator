import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

def scrape_amazon_page(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    product_divs = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
    scraped_data = []
    for product_div in product_divs:
        try:
            product_title_element = product_div.find_element(By.XPATH, './/h2/a/span')
            product_title = product_title_element.text
            price_element = product_div.find_element(By.XPATH, './/span[@class="a-price"]')
            price = price_element.text
            scraped_data.append({'name': product_title, 'price': price})
        except Exception as e:
            print("Error occurred:", str(e))
    driver.quit()
    return scraped_data

def scrape_flipkart_page(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    product_divs = driver.find_elements(By.XPATH, "//div[@class='_75nlfW']")
    scraped_data = []
    for product_div in product_divs:
        try:
            name = product_div.find_element(By.CLASS_NAME, 'KzDlHZ').text
            price = product_div.find_element(By.CLASS_NAME, 'Nx9bqj').text
            scraped_data.append({'name': name, 'price': price})
        except Exception as e:
            print("Error occurred:", str(e))
    driver.quit()
    return scraped_data

def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def load_from_csv(filename):
    data = []
    if os.path.exists(filename):
        with open(filename, 'r', newline='', encoding='utf-8') as input_file:
            dict_reader = csv.DictReader(input_file)
            for row in dict_reader:
                data.append(row)
    return data

amazon_data = []
num_pages = 5
for page_num in range(1, num_pages + 1):
    url = f"https://www.amazon.in/s?k=iphone&qid=1713807378&ref=sr_pg_{page_num}"
    print("Scraping Amazon page:", page_num)
    amazon_data.extend(scrape_amazon_page(url))
    time.sleep(2)

flipkart_data = []
for page_num in range(1, 10):
    url = f"https://www.flipkart.com/mobiles/apple~brand/pr?sid=tyy%2C4io&page={page_num}"
    print("Scraping Flipkart page:", page_num)
    flipkart_data.extend(scrape_flipkart_page(url))
    time.sleep(10)

# Save data to CSV
save_to_csv(amazon_data, 'amazon_data.csv')
save_to_csv(flipkart_data, 'flipkart_data.csv')
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from rake_nltk import Rake

flipkart_df = pd.read_csv('flipkart_data.csv')
amazon_df = pd.read_csv('amazon_data.csv')

def extract_keywords(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()

def search_best_match(keywords):
    flipkart_results = []
    amazon_results = []

    for index, row in flipkart_df.iterrows():
        for keyword in keywords:
            if keyword.lower() in row['name'].lower():
                flipkart_results.append(row)
                break
    
    for index, row in amazon_df.iterrows():
        for keyword in keywords:
            if keyword.lower() in row['name'].lower():
                amazon_results.append(row)
                break

    return flipkart_results, amazon_results

def compare_prices(flipkart_results, amazon_results):
    if not flipkart_results or not amazon_results:
        print("No matching results found.")
        return
    
    flipkart_price = min(flipkart_results, key=lambda x: x['price'])['price']
    amazon_price = min(amazon_results, key=lambda x: x['price'])['price']

    print("Best Match (Flipkart):", flipkart_results[0]['name'])
    print("Flipkart Price:", flipkart_price)
    print("Best Match (Amazon):", amazon_results[0]['name'])
    print("Amazon Price:", amazon_price)

search_query = input("Enter the item you want to search for: ")

exact_flipkart_results = flipkart_df[flipkart_df['name'].str.lower().str.contains(search_query.lower())]
exact_amazon_results = amazon_df[amazon_df['name'].str.lower().str.contains(search_query.lower())]

if exact_flipkart_results.empty and exact_amazon_results.empty:
    keywords = extract_keywords(search_query)
    flipkart_results, amazon_results = search_best_match(keywords)
    compare_prices(flipkart_results, amazon_results)
else:
    flipkart_price = min(exact_flipkart_results['price'])
    amazon_price = min(exact_amazon_results['price'])
    print("(Flipkart):", exact_flipkart_results.iloc[0]['name'])
    print("Flipkart Price:", flipkart_price)
    print("(Amazon):", exact_amazon_results.iloc[0]['name'])
    print("Amazon Price:", amazon_price)
