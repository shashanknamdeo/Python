def totp():
    import pyotp
    totp= pyotp.TOTP('ROHOBQKIHWAT23UFAXGV5HEEGKLZN6P4')
    totp_pin = totp.now()
    return totp_pin

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path=r'D:\NotebookShareAsus\SoftwareInstalled\ChromeWebDriver\chromedriver_v106.exe')
browser.get('https://kite.zerodha.com')

user_id_element = browser.find_element("id", "userid")
password_element = browser.find_element("id", "password")
user_id_element.send_keys("ZPK273")
password_element.send_keys("_Shashank28")
browser.find_element("xpath",'//*[@id="container"]/div/div/div/form/div[4]/button').click()

import time
time.sleep(5)
totp_element = browser.find_element("xpath",'//*[@id="container"]/div/div/div/form/div[2]/input')
totp_element.send_keys(totp())
browser.find_element("xpath",'//*[@id="container"]/div/div/div/form/div[3]/button').click()



