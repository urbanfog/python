from bs4 import BeautifulSoup
import requests
import smtplib
import os

# Load ENV variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

target_product_name = input('What product are you looking for? ')
target_product_price = float(
    input(f"What is your target price for the {target_product_name}? $"))
target_product_url = input(
    "Where can the item be found? Please enter url here: ")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_EMAIL_PW")

# testing
# target_product_url = "https://www.amazon.ca/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
# target_product_name = "Instant Pot"
# target_product_price = 170


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Accept-Language": "en-US,en;q=0.5",
}


def send_email(message, send_to):
    '''Use stmplib module to send email'''
    msg = f"Price Alert: {target_product_name}\n\n{message}".encode(
        encoding="utf8")
    with smtplib.SMTP("smtp.live.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=send_to,
                            msg=msg)


# Scrape Amazon for price and convert into float
response = requests.get(url=target_product_url, headers=headers).text
soup = BeautifulSoup(response, "lxml")
try:
    current_price = float(
        soup.find(id="priceblock_ourprice").getText().split("$")[1])
    if current_price <= target_product_price:
        send_email(send_to="jamescsmith@live.com",
                   message=f"{target_product_name} is currently {current_price} which is at or below target price of {target_product_price}.\nBuy it here: {target_product_url}")
except AttributeError:
    print("Cannot find the price object. Item may not be available.")
