from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 

s = Service(r'C:\Users\user\Desktop\drivers\chromedriver.exe')
browser=webdriver.Chrome(service=s)
print("First Program started")
browser.get('https://www.google.com/')
browser.maximize_window()
time.sleep(2)

search_input=browser.find_element_by_name('q')
search_input.send_keys('bhavya')
time.sleep(2)

search_button=browser.find_element_by_css_selector('input[type="submit"]')
search_button.click()
time.sleep(2)
click_link=browser.find_element_by_css_selector('a[href="https://www.instagram.com/bhavyagandhi97/?hl=en"]')
click_link.click()
