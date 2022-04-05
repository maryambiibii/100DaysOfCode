import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/Yours/Development/chromedriver"
TWITTER_EMAIL = Your_Email
TWITTER_PASSWORD = Your_Password
USER_NAME = Your_Username


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down, self.up = self.get_internet_speed()

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net')

        time.sleep(3)

        start_test = self.driver.find_element(By.CSS_SELECTOR, '.start-text')
        start_test.click()

        time.sleep(60)

        self.down = self.driver.find_element(By.CSS_SELECTOR, '.result-item-download .result-data-value')
        self.up = self.driver.find_element(By.CSS_SELECTOR, '.result-item-upload .result-data-value')

        print("down: ", self.down.text)
        print("up: ", self.up.text)

        return self.down.text, self.up.text

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(2)

        email = self.driver.find_element(By.NAME, 'text')
        email.send_keys(TWITTER_EMAIL)
        time.sleep(1)

        email.send_keys(Keys.ENTER)
        time.sleep(2)

        username = self.driver.find_element(By.NAME, 'text')
        username.send_keys(USER_NAME)
        time.sleep(1)

        username.send_keys(Keys.ENTER)
        time.sleep(2)

        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(1)

        password.send_keys(Keys.ENTER)

        time.sleep(5)

        tweet = f'Hey Internet Provider, why is my internet speed is {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?'
        tweet_label = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_label.send_keys(tweet)

        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.send_keys(Keys.ENTER)


internet_speed_twitter_bot = InternetSpeedTwitterBot()
internet_speed_twitter_bot.tweet_at_provider()
