# Smart-Price-Comparator
SmartPriceComparator is a Python-based price tracking and comparison tool that automates product data extraction from Amazon, Flipkart, and Nykaa using Selenium and BeautifulSoup. It collects prices, ratings, reviews, and features, stores them in CSV files, and uses NLP keyword matching to identify the best available deal.

# Price Comparison and E-Commerce Web Scraping Tool

This project is a Python-based web scraping and price comparison system designed to extract product information from major e-commerce platforms, including Amazon, Flipkart, and Nykaa. It automates data collection using Selenium and BeautifulSoup, stores data in CSV format, and performs keyword-based product matching and price comparison.

The project includes multiple modules for scraping, data extraction, keyword analysis, and direct URL price checking.

---

## Features

### 1. Automated Product Scraping (Amazon & Flipkart)

* Scrapes product listings using Selenium WebDriver.
* Extracts key attributes such as:

  * Product name
  * Price (discounted and original)
  * Ratings
  * Reviews count
  * Product features
  * Discounts
* Handles multiple pages of search results.

### 2. Direct URL Price Checker

* Fetches product price directly using a product URL.
* Supports Amazon, Flipkart, and Nykaa.
* Built with Requests and BeautifulSoup.


### 3. CSV Data Storage and Retrieval

* Automatically saves scraped data into CSV files.
* Supports loading the data back for analysis.


### 4. Keyword-Based Product Matching (NLP)

* Uses RAKE (Rapid Automatic Keyword Extraction) to find the closest matching product when the exact name is not provided.
* Compares prices between Amazon and Flipkart using extracted keywords.

### 5. Selenium Driver Setup Included

* Contains a predefined ChromeDriver setup file.


## Technologies Used

* Python
* Selenium WebDriver
* BeautifulSoup (BS4)
* Requests
* Pandas
* RAKE-NLTK
* ChromeDriver
* CSV Data Handling

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Configure ChromeDriver

Download the appropriate ChromeDriver version based on your browser and update the path in:

```
chromedriver_setup.py
```

---

## Usage

### Run Amazon and Flipkart Scraper

```
python amazon_flipkart_scraper.py
```

### Run Advanced Flipkart Scraper

```
python flipkart_advanced_scraper.py
```

### Run Direct URL Price Checker

```
python price_checker_bs4.py
```

### Run NLP-Based Price Comparison

```
python amazon_flipkart_scraper_v2.py
```

---

## Output Details

Depending on the script, the system outputs:

* Product Name
* Discounted Price
* Original Price
* Ratings
* Reviews Count
* Product Features
* Extracted Keywords
* Cheapest Price Between Platforms
* CSV files containing complete scraped datasets

---

## Future Enhancements

* Integration with a database (MongoDB or PostgreSQL)
* Web-based dashboard for visualization
* Proxy rotation and advanced anti-bot handling
* Multi-site integration (Croma, Reliance Digital, Tata Cliq)
* Automated email alerts on price drops

---

## Author

Kartik Arora
B.Tech in Computer Science Engineering (Cybersecurity)
UPES Dehradun


