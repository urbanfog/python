from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pprint import pprint
import pandas as pd

chrome_driver_path = "/Users/smith/chromedriver"
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option(
    "prefs", {'profile.managed_default_content_settings.javascript': 2})

driver = webdriver.Chrome(executable_path=chrome_driver_path)
filename = '/Users/smith/python/100DaysofPython/airdrie_props.csv'


roll_data = pd.read_csv(
    '/Users/smith/python/100DaysofPython/Residential_Title_Transfers.csv')

# Update before running
start_num = 249
total_num = 5689
roll_nums = roll_data['Tax Roll'].tolist()[start_num:]
temp_data = []


def scrape():
    i = start_num
    for num in roll_nums:
        # Main Page Set up
        driver.get("https://www.airdrie.ca/index.cfm?serviceID=284")
        time.sleep(0.5)
        field = driver.find_element_by_name('rollNumber')
        button = driver.find_element_by_name('taxrollSubmit')

        field.send_keys(num)
        button.click()
        time.sleep(1)
        row = {}
        # Table 1
        row['address'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/div/table/thead/tr/th').text
        row['roll'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/div/table/tbody/tr[1]/td').text
        row['legal_desc'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/div/table/tbody/tr[2]/td').text
        row['assessed_value'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/div/table/tbody/tr[3]/td').text
        row['land_use.append'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/div/table/tbody/tr[4]/td').text
        row['classifications'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/div/table/tbody/tr[5]/td').text
        row['parcel_area'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/div/table/tbody/tr[6]/td').text

        # Table 2
        row['year_built'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/table/tbody/tr[1]/td').text
        row['living_area_above_grade'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/table/tbody/tr[2]/td').text
        row['bldg_desc.append'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/table/tbody/tr[3]/td').text
        row['finished_below_grade'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/table/tbody/tr[4]/td').text
        row['garage'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/table/tbody/tr[5]/td').text
        row['deck'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/table/tbody/tr[6]/td').text
        row['veranda'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/table/tbody/tr[7]/td').text
        row['fireplace'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/table/tbody/tr[8]/td').text
        row['walkout_basement'] = driver.find_element_by_xpath(
            '//*[@id="assessmentResultContainer"]/table/tbody/tr[9]/td').text
        temp_data.append(row)
        time.sleep(1)
        i += 1
        print(f"{i} of {total_num}")
    driver.quit()


def save_to_df():
    # Create Dataframe
    df = pd.DataFrame(temp_data)
    df.to_csv("airdrie_props.csv")


scrape()
save_to_df()
