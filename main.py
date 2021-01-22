from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Credentials
USERNAME = input('Enter your username: ')
PASSWORD = input('Enter your password: ')

# Victim
VICTIM_USERNAME = input('Enter victim username: ')
MESSAGE = input('Enter message: ')
QUANTITY = int(input('Enter quantity: '))

# Advanced configurations
SLEEPING_DELAY = 3

# Init chrome session
chrome = webdriver.Chrome('C:\\chromedriver.exe')

# Enter to instagram
chrome.get(f'https://www.instagram.com/{VICTIM_USERNAME}/')
time.sleep(2)

# Login to instagram
login_button = chrome.find_element_by_class_name('y3zKF')
login_button.click()


username_field = chrome.find_element_by_name('username')
username_field.send_keys(USERNAME)


password_field = chrome.find_element_by_name('password')
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(SLEEPING_DELAY)

skip_button = chrome.find_element_by_class_name('yWX7d')
skip_button.click()

# Finding victim
contact_button = chrome.find_element_by_class_name('_8A5w5')
contact_button.click()
time.sleep(SLEEPING_DELAY)
contact_button = chrome.find_element_by_class_name('HoLwm')
contact_button.click()

text_bar = chrome.find_element_by_tag_name('textarea')

for i in range(0, QUANTITY):
    text_bar.send_keys(MESSAGE)
    text_bar.send_keys(Keys.ENTER)












