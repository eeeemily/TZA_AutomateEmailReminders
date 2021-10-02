# Selenium: Automate Email Reminder sending
# Minghui Zheng @2021
# references: password session: https://www.youtube.com/watch?v=iJGvYBH9mcY&ab_channel=PythonSimplified
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

# Other imports here
import os
PATH = "C:\Program Files\Python\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = "https://rochester.mywconline.com/index.php"
username = os.environ.get('TZA_user')
password = os.environ.get('TZA_password')

driver.get(url)
time.sleep(1)  # give it some time to load
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_value("sc6123e04a854a5").click()

# driver.find_element_by_name("login").click()
