from selenium import webdriver

chrome_driver_path = "/Users/smith/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
events_dict = {}

event_titles = driver.find_elements_by_css_selector(
    "div.medium-widget.event-widget ul li a")

event_times = driver.find_elements_by_css_selector(
    "div.medium-widget.event-widget ul li time")

for index, event in enumerate(event_titles):
    events_dict[index] = {'time': event_times[index].text, 'name': event.text}
print(events_dict)
driver.quit()
