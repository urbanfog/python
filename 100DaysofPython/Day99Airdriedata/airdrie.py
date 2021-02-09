from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pprint import pprint
import pandas as pd
from bs4 import BeautifulSoup
import re

chrome_driver_path = "/Users/smith/chromedriver"
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option(
    "prefs", {'profile.managed_default_content_settings.javascript': 2})

driver = webdriver.Chrome(executable_path=chrome_driver_path)
filename = '/Users/smith/python/100DaysofPython/Day99Airdriedata/airdrie_props.csv'


roll_data = pd.read_csv(
    '/Users/smith/python/100DaysofPython/Day99Airdriedata/Residential_Title_Transfers.csv')


def scrape(num):
    # Main Page Set up
    driver.get("https://www.airdrie.ca/index.cfm?serviceID=284")
    time.sleep(0.5)
    field = driver.find_element_by_name('rollNumber')
    button = driver.find_element_by_name('taxrollSubmit')

    field.send_keys(num)
    button.click()
    time.sleep(0.5)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    row = {
        'address': "n/a",
        'roll': "n/a",
        'legal_desc': "n/a",
        'assessed_value': "n/a",
        'land_use': "n/a",
        'classifications': "n/a",
        'parcel_area': "n/a",
        'year_built': "n/a",
        'living_area_above_grade': "n/a",
        'bldg_desc': "n/a",
        'finished_below_grade': "n/a",
        'garage': "n/a",
        'deck': "n/a",
        'veranda': "n/a",
        'fireplace': "n/a",
        'walkout_basement': "n/a",
    }

    # Table 1
    row['address'] = re.sub('\s+', ' ', soup.select(
        '#assessmentResultContainer > div > table > thead > tr > th')[0].get_text().strip())
    row['roll'] = re.sub('\s+', ' ', soup.select(
        '#assessmentResultContainer > div > table > tbody > tr:nth-child(1) > td')[0].get_text().strip())
    row['legal_desc'] = re.sub('\s+', ' ', soup.select(
        '#assessmentResultContainer > div > table > tbody > tr:nth-child(2) > td')[0].get_text().strip())
    row['assessed_value'] = re.sub('\s+', ' ', soup.select(
        '#assessmentResultContainer > div > table > tbody > tr:nth-child(3) > td')[0].get_text().strip())
    row['land_use'] = re.sub('\s+', ' ', soup.select(
        '#assessmentResultContainer > div > table > tbody > tr:nth-child(4) > td')[0].get_text().strip())
    row['classifications'] = re.sub('\s+', ' ', soup.select(
        '#assessmentResultContainer > div > table > tbody > tr:nth-child(5) > td')[0].get_text().strip())
    if soup.select(
            '#assessmentResultContainer > div > table > tbody > tr:nth-child(6) > td'):
        row['parcel_area'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > div > table > tbody > tr:nth-child(6) > td')[0].get_text().strip())

    # Table 2
    if soup.select('#assessmentResultContainer > table > tbody > tr:nth-child(1) > th')[0].get_text() == 'Year Built':
        row['year_built'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(1) > td')[0].get_text().strip())
        row['living_area_above_grade'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(2) > td')[0].get_text().strip())
        row['bldg_desc'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(3) > td')[0].get_text().strip())
        row['finished_below_grade'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(4) > td')[0].get_text().strip())
        row['garage'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(5) > td')[0].get_text().strip())
        row['deck'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(6) > td')[0].get_text().strip())
        row['veranda'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(7) > td')[0].get_text().strip())
        row['fireplace'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(8) > td')[0].get_text().strip())
        row['walkout_basement'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(9) > td')[0].get_text().strip())
    elif 'Living Area' in soup.select('#assessmentResultContainer > table > tbody > tr:nth-child(1) > th')[0].get_text():
        row['living_area_above_grade'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(1) > td')[0].get_text().strip())
        row['bldg_desc'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(2) > td')[0].get_text().strip())
        row['finished_below_grade'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(3) > td')[0].get_text().strip())
        row['garage'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(4) > td')[0].get_text().strip())
        row['deck'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(5) > td')[0].get_text().strip())
        row['veranda'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(6) > td')[0].get_text().strip())
        row['fireplace'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(7) > td')[0].get_text().strip())
        row['walkout_basement'] = re.sub('\s+', ' ', soup.select(
            '#assessmentResultContainer > table > tbody > tr:nth-child(8) > td')[0].get_text().strip())
    else:
        print(f"num: {num}, error")Í
    return row


def save_to_df(row):
    print(row)
    with open("/Users/smith/python/100DaysofPython/Day99Airdriedata/airdrie_props.csv", mode="a") as file:
        file.write(f"{row['address']},{row['roll']},{row['legal_desc']},{row['assessed_value']},{row['land_use']},{row['classifications']},{row['parcel_area']},{row['year_built']},{row['living_area_above_grade']},{row['bldg_desc']},{row['finished_below_grade']},{row['garage']},{row['deck']},{row['veranda']},{row['fireplace']},{row['walkout_basement']}\n")


# Update before running
start_num = 3924
total_num = 5689
roll_nums = roll_data['Tax Roll'].tolist()[start_num:]
df = pd.DataFrame()
i = start_num

for num in roll_nums:
    print(num)
    row = scrape(num)
    save_to_df(row)
    i += 1
    print(f"{i} of {total_num}")
