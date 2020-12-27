from string import Template
from selenium import webdriver
import os
import time
from selenium.common.exceptions import ElementClickInterceptedException

# Load ENV variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)


INSTA_EMAIL = os.getenv("INSTA_EMAIL")
INSTA_PASS = os.getenv("INSTA_PASS")
TEMPLATE_ACCOUNT = "thecookingguy"


class InstaFollowerBot:
    def __init__(self) -> None:
        chrome_driver_path = "/Users/smith/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        username = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        username.send_keys(INSTA_EMAIL)
        password.send_keys(INSTA_PASS)
        time.sleep(1)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()

    def find_followers(self, account):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{account}")

        time.sleep(2)
        followers = self.driver.find_element_by_partial_link_text("followers")
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        buttons = self.driver.find_elements_by_css_selector("li button")
        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollowerBot()
bot.login()
bot.find_followers(TEMPLATE_ACCOUNT)
bot.follow()
