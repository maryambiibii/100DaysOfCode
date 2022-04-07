import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = 'your_driver_pyth'
FORM_ADDRESS = 'your_form_address'

#################################### BeautifulSoup for Scrapping Zillow ########################################
response = requests.get("https://www.zillow.com/new-ulm-mn/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22323%20N%20German%20St%20%23304%20New%20Ulm%2C%20MN%2056073%22%2C%22mapBounds%22%3A%7B%22west%22%3A-94.47059601545334%2C%22east%22%3A-94.45188492536545%2C%22south%22%3A44.312922998984355%2C%22north%22%3A44.321812129245735%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A42727%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A386566%7D%2C%22mp%22%3A%7B%22max%22%3A1600%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A16%7D", headers={"Accept-Language":"","User-Agent":""})
zillow_text = response.text

soup = BeautifulSoup(zillow_text, "html.parser")

addresses = soup.find_all(class_="list-card-addr")
addresses_list = []
for address in addresses:
    add = address.getText()
    addresses_list.append(add)
print(addresses_list)

prices = soup.find_all(class_="list-card-price")
price_list = []
for price in prices:
    p = price.getText()
    price_list.append(p)
print(price_list)

links = soup.find_all(class_="list-card-img")
link_list = []
for link in links:
    ind_link = link.get('href')
    link_list.append(ind_link)
print(link_list)

listing = zip(addresses_list, price_list, link_list)
listing_list = list(listing)
print(listing_list)
print(listing_list[0][0])

#################################### Selenium for Filling the Form ########################################

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(FORM_ADDRESS)

time.sleep(3)


for data in listing_list:
    address_label = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_label.send_keys(data[0])
    time.sleep(3)

    price_label = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_label.send_keys(data[1])
    time.sleep(3)

    link_label = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_label.send_keys(data[2])
    time.sleep(3)

    submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_btn.click()

    submit_another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_response.click()

    time.sleep(5)



