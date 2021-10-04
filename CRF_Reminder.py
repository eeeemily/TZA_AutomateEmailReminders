# Selenium: Automate Email Reminder sending
# Minghui Zheng @2021
# references: password session: https://www.youtube.com/watch?v=iJGvYBH9mcY&ab_channel=PythonSimplified
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import missingCRF
import time

# Other imports here
import os
PATH = "C:\Program Files\Python\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = "https://rochester.mywconline.com/index.php"
CRFurl = "https://rochester.mywconline.com/report_mlr.php"
username = os.environ.get('TZA_user')
password = os.environ.get('TZA_password')

try:
    # step 1: log into the 2021 Fall CETL Tutoring Schedule
    driver.get(url)
    # time.sleep(1)  # give it some time to load
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    # driver.find_element_by_css_selector(
    #     'input[value="sc6123e04a854a5"]').click()
    driver.find_element_by_name("login").click()

    # step 2: navigate to master listing page
    driver.get(CRFurl)

    # step 3: select start and end date
    # Scheudle Limit -> 2021 Fall CETL Tutoring
    driver.find_element_by_css_selector(
        'option[value="sc60da1cb288473"]').click()
    # Content: Orphan Appointment only
    driver.find_element_by_css_selector(
        'option[value="orphan"]').click()
    # starting date
    startDatePicker = driver.find_element_by_css_selector(
        'input[name="sdate"]')
    startDatePicker.clear()
    startDatePicker.send_keys("October 1, 2021")
    # ending date
    endDatePicker = driver.find_element_by_css_selector(
        'input[name="edate"]')
    endDatePicker.clear()
    endDatePicker.send_keys("October 2, 2021")
    # Run Report!
    driver.find_element_by_name("submit").click()

    # step 4: make each entry in the row into a list

    missingCRFCollection = []

    index = 3

    test = driver.find_element_by_xpath(
        (f"(//*[starts-with(@style, 'padding-bottom:0px;font-size:14px;padding-top:5px;')]//b)[{index}]"))
    print(test.text)

    for idx in range(4, 21):
        print(idx)
        tName = driver.find_element_by_xpath(
            (f"(//*[starts-with(@style, 'padding-bottom:0px;font-size:14px;padding-top:5px;')]//b)[{idx}]"))
        print(tName.text)
        sDate = driver.find_element_by_xpath(
            f"(//*[starts-with(@style, 'width:25%')]//p//b)[{idx}]")
        print(sDate.text)
        # sTime = driver.find_element_by_xpath(
        #     "(//*[starts-with(@style, 'width:25%;float:left')]//p[text()]")
        # print(sTime)

    # for c in missingCRFCollection:
    #     c.printInfo()
except:
    print("something is wrong!")
