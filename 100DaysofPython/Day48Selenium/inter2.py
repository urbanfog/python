from selenium import webdriver

# Task: Scrape wikipedia page, grab current number of articles

chrome_driver_path = "/Users/smith/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name('fName')
last_name = driver.find_element_by_name('lName')
email = driver.find_element_by_name('email')
button = driver.find_element_by_class_name('btn.btn-lg.btn-primary.btn-block')

first_name.send_keys("First")
last_name.send_keys("Last")
email.send_keys("email@test.com")
button.click()
