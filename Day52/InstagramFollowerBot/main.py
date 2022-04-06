import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = '/Users/your_path/Development/chromedriver'
SIMILAR_ACCOUNT = 'chefsteps'
USERNAME = Your_username
PASSWORD = Your_password


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get('https://www.instagram.com')
        time.sleep(3)

        user_name = self.driver.find_element(By.NAME, 'username')
        user_name.send_keys(USERNAME)

        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_btn.send_keys(Keys.ENTER)

        time.sleep(10)

        save_info = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        save_info.send_keys(Keys.ENTER)

        time.sleep(5)

        notification = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]')
        notification.send_keys(Keys.ENTER)

    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')
        time.sleep(3)

        followers_link = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_link.send_keys(Keys.ENTER)

        time.sleep(5)

        followers_popup = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        scroll = 0
        while scroll < 10:  # scroll 5 times
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', followers_popup)
            time.sleep(2)
            scroll += 1

    def follow(self):
        followers_popup = self.driver.find_elements(By.CSS_SELECTOR, '.isgrP .y3zKF')
        for follower in followers_popup:
            try:
                follower.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_unfollow = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_unfollow.click()
                time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
