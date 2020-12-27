import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import lxml
import re

rental_links = []
rental_prices = []
rental_addresses = []


def scrape_zillow():
    global rental_addresses, rental_links, rental_prices

    # 1 Create Soup out of Zillow page
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0",
    }
    zillow_page = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
    response = requests.get(zillow_page, headers=headers).text
    stew = BeautifulSoup(response, "lxml")

    # 2 Create list of links from scrape
    for link in stew.find_all(class_="list-card-link"):
        href = link["href"]
        if "http" not in href:
            rental_links.append(f"https://www.zillow.com{href}")
        else:
            rental_links.append(href)

    # 3 Create list of prices
    rental_prices = [price.getText()
                     for price in stew.find_all(class_="list-card-price")]

    # 4 Create list of addresses
    rental_addresses = [address.getText()
                        for address in stew.find_all(class_="list-card-addr")]
    print(
        f"links: {len(rental_links)}, addys: {len(rental_addresses)}, prices: {len(rental_prices)}")


chrome_driver_path = "/Users/smith/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


def fill_in_google_form():
    # 5 Use Selenium to fill in Google form with above info
    google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLScSUHkPClEy02VJIkd7wJgEBaTlvYEv9xP8E-F7-Sn_Mcqv-g/viewform?usp=sf_link"

    # Find various attributes on google form, iterating through as webpage redirects
    for index, rental in enumerate(rental_addresses):
        print(f"{index} of {len(rental_addresses) - 1}")
        driver.get(google_form_link)
        time.sleep(3)
        address_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        url_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_button = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')

    # Iterate through lists and populate forms
        time.sleep(1)
        address_field.send_keys(rental)
        price_field.send_keys(rental_prices[index])
        url_field.send_keys(rental_links[index])
        submit_button.click()


def create_google_sheet():
    # 6 After all data entered, click on create google sheet button
    admin_page = driver.get(
        "https://docs.google.com/forms/d/1gdv5cFdnl8D-Mjn27YKAMQM8iKtjj59p_cxmS2t6ZxA/edit")
    responses_tab = driver.find_element_by_xpath(
        '/html/body/div[3]/div[1]/div[1]/div[3]/div[1]/div/div[2]/span/div')
    responses_tab.click()

    google_sheet_button_xpath = driver.find_element_by_xpath(
        '/html/body/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div/span')
    google_sheet_button_xpath.click()


scrape_zillow()
fill_in_google_form()
create_google_sheet()

driver.quit()
