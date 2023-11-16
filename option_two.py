# We use selenium, not as efficient as requests, but we can get the estimated earnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import random
import re
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import csv
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
import os
import concurrent.futures
import threading

def options():

    options = ChromeOptions()
    # Activem javascript
    options.add_argument("--enable-javascript")
    # Associem al driver un useragent humà
    options.add_argument \
        ("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    #options.add_argument("--headless")
    # Desactivem les blink features
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Configurem la proxy a las opcions del driver
    # Desactivem el carregat d'imatges.
    options.add_argument("--disable-image-loading")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-popup-blocking")
    return options



def webdriver_example():

    # El creem amb les opcions de la proxy escollida cridant a la funcio smartproxy anterior.
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                               options=options())

    return browser

url = "https://www.realtor.com/realestateandhomes-detail/Carr-131-Calle-2-Bo-Guilarte-Adjuntas-Puerto-Rico-Unit-122_Adjuntas_PR_00601_M92732-14747"

driver = webdriver_example()
driver.get(url)
time.sleep(5)
html_content = driver.page_source
# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
print(soup)
address_span = soup.find('h1', class_='LDPHomeFactsstyles__H1-sc-11rfkby-3 ibiqDI')
address = address_span.text
price = soup.find('div', class_="Pricestyles__StyledPrice-rui__btk3ge-0 bvgLFe LDPListPricestyles__StyledPrice-sc-1m24xh0-1 jyBxDQ")
price = price.text
ldp_home_facts_div = soup.find('div', {'data-testid': 'ldp-home-facts'})
# Initialize variables for storing information
beds = baths = sqft = acre_lot = None

# Check if the div is found
if ldp_home_facts_div:
    # Find each li tag within the div and extract the text content
    li_elements = ldp_home_facts_div.find_all('li')
    if li_elements:
        # Extract text content from each li tag
        beds = li_elements[0].find('span', {'data-testid': 'meta-value'}).text.strip()
        baths = li_elements[1].find('span', {'data-testid': 'meta-value'}).text.strip()
        sqft = li_elements[2].find('span', {'data-testid': 'meta-value'}).text.strip()
        acre_lot = li_elements[3].find('span', {'class': 'meta-value', 'data-testid': 'meta-value'}).text.strip()
all_data = soup.find_all('div',
                              class_='base__StyledType-rui__sc-108xfm0-0 gMZrrg listing-key-fact-item__value')
estimated_earnings = soup.find('span', class_='Pricestyles__StyledPrice-rui__btk3ge-0 bvgLFe').text.strip()
property_type = all_data[0].text.strip()
days_on_realtor = all_data[1].text.strip()
price_per_sqft = all_data[2].text.strip()
year_built = all_data[3].text.strip()
# Print or use the extracted information as needed
print('Address:', address)
print('Price:', price)
print('Beds:', beds)
print('Baths:', baths)
print('Sqft:', sqft)
print('Acre:', acre_lot)
print('Property type:', property_type)
print('Price_per_sqft:', price_per_sqft)
print('Days on Realtor:', days_on_realtor)
print('Year built', year_built)
print('Estimated earnings:', estimated_earnings)
