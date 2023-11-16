# We use requests, faster more efficient, simpler but we can not get the estimated_earnings per building because it loads via javascript in the html code, so requests can't get it.
import requests
from bs4 import BeautifulSoup
url = "https://www.realtor.com/realestateandhomes-detail/Carr-131-Calle-2-Bo-Guilarte-Adjuntas-Puerto-Rico-Unit-122_Adjuntas_PR_00601_M92732-14747"
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
response = requests.get(url,headers=headers)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
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
else:
    print(response.status_code)
