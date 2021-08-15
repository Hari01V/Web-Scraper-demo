from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get(
    'https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=775ba9be-2e89-47a0-8b5e-ca74080984f1'
)

soup = BeautifulSoup(driver.page_source)
# print(soup)
links = soup.findAll('a', href=True, attrs={'class': '_1fQZEK'})

Pname = []
Pdesc = []
Pprice = []
Poffer = []
Prating = []

for item in links:
    name = item.find('div', attrs={'class': '_4rR01T'})
    desc_list_items = item.findAll('li', attrs={'class': 'rgWa7D'})
    desc = ""
    for list_item in desc_list_items:
        desc += list_item.text + " ..... "
    price = item.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
    offer_div = item.find('div', attrs={'class': '_3Ay6Sb'})
    if offer_div:
        offer = offer_div.find('span').text
    else:
        offer = "No Offer"
    rating = item.find('div', attrs={'class': '_3LWZlK'})

    Pname.append(name.text)
    Pdesc.append(desc)
    Pprice.append(price.text)
    Poffer.append(offer)
    Prating.append(rating.text)

# STORE THE EXTRACTED DATA
data = pd.DataFrame({
    'Name': Pname,
    'Desc': Pdesc,
    'Price': Pprice,
    'Offer': Poffer,
    'Rating': Prating
})
data.to_excel('flipkart_laptop.xlsx', sheet_name='Flipkart_sheet')

# CLOSES THE TAB
# driver.close()

# CLOSE THE BROWSER
driver.quit()