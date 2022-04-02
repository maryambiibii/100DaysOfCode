import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Creating drivers
chrome_driver_path = "/Users/maryammehboob/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

click_cookie = driver.find_element(By.ID, 'cookie')

game_end_time = time.time() + 60*1
start = time.time()
purchase_time = 5
game_ = True
while game_:
    if time.time() - start < purchase_time:
        click_cookie.click()
    else:
        money = driver.find_element(By.ID, "money")
        cookies_money = money.text
        affordable_purchases = driver.find_elements(By.CSS_SELECTOR, "div[class='']")
        item_price = []
        items_purchases = {}
        for elem in affordable_purchases:
            purchase_id = elem.get_attribute("id")
            purchase_price = driver.find_element(By.CSS_SELECTOR, f"#{purchase_id} b")
            purchase_price_str = purchase_price.text
            affordable_item_price = purchase_price_str.split('- ')[1]
            item_price.append(int(affordable_item_price))
            items_purchases[int(affordable_item_price)] = purchase_id

        #print(items_purchases)
        a = np.array(item_price)
        expensive_purchase = a[np.abs(a - int(cookies_money)).argmin()]
        #print(expensive_purchase)
        most_exp_item = items_purchases[expensive_purchase]
        exp_item = driver.find_element(By.ID, f"{most_exp_item}")
        exp_item.click()

        if time.time() > game_end_time:
            cookies_per_second = driver.find_element(By.ID, "cps")
            print(cookies_per_second.text)
            game_ = False
        purchase_time += 5
