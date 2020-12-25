from selenium import webdriver
import time

chrome_driver_path = "/Users/smith/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")
score = 0


def check_score():
    global score
    score = int(driver.find_element_by_id("cookies").text.split(" ")[0])
    print(score)


def check_for_upgrades():
    upgrades = driver.find_elements_by_css_selector(
        "#products #storeBulk .content .price")
    max_price = 0
    max_index = 0
    for index, upgrade in enumerate(upgrades):
        current = int(upgrade.text)
        if current > max_price and current < score:
            max_price = current
            max_index = index

    to_buy = driver.find_element_by_xpath(
        f'//*[@id="productPrice{max_index}"]')
    to_buy.click()


timeout = 300
timeout_start = time.time()
while time.time() < timeout_start + timeout:
    time.sleep(0.05)
    cookie.click()
    if time.time() % 5000:
        pass
        check_score()
        # check_for_upgrades()
cookie_per_sec = driver.find_element_by_xpath(
    '//*[@id="cookies"]/div').text.split(" : ")[1]
print(cookie_per_sec)
driver.quit()
