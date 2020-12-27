from selenium import webdriver
import os
import time

# Load ENV variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)


PROMISED_UP = 150
PROMISED_DOWN = 150
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASS = os.getenv("TWITTER_PASS")


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        chrome_driver_path = "/Users/smith/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element_by_class_name("start-text")
        start_button.click()

        time.sleep(45)

        self.down = float(self.driver.find_element_by_class_name(
            "download-speed").text)
        self.up = float(
            self.driver.find_element_by_class_name("upload-speed").text)
        print(f"Download: {self.down}, upload: {self.up}")
        self.driver.quit()

    def tweet_at_provider(self):
        if PROMISED_DOWN > self.down and PROMISED_UP > self.up:

            self.driver.get("https://twitter.com/")
            btn = self.driver.find_element_by_link_text("Log in")
            btn.click()

            # sign in
            time.sleep(2)
            email = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
            email.click()
            email.send_keys(TWITTER_EMAIL)
            password = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
            password.click()
            password.send_keys(TWITTER_PASS)
            btn = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div/span/span')
            btn.click()

            # Tweet page
            time.sleep(2)
            text_field = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
            message = f"Hey Telus, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_UP}up/{PROMISED_DOWN}down"
            text_field.send_keys(message)

            time.sleep(1)
            tweet_button = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')

            tweet_button.click()
            self.driver.quit()
        else:
            print(
                f"No need to tweet. Internet speed {self.down}down/{self.up}up vs. {PROMISED_UP}up/{PROMISED_DOWN}down")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
