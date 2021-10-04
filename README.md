To use this reminder automation

1. Add pip to the path, make sure it's working

- Windows:
  1. open up "Command Prompt"
  2. type "pip install -U selenium" and hit enter
- Mac
  1. Open up "terminal"
  2. type "pip3 install selenium"

2. To Run on Windows:
   a. "cd [yourpath/]" e.g. "cd C:\Users\emily\Desktop\Repos\TZA_AutomateEmailReminders"
   b. "py CRF_Reminder.py"

Errors you might run in to and how to fix them:

1. Selenium doesn't support the neweer version of Chrome.
   e.g.
   "selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 92"
   Solution: download a the correct version of webdriver from https://chromedriver.chromium.org/downloads, and replaced the driver file on the path
