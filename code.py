"""
Install selenium by pip install selenium
also download the chroedriver from 'https://chromedriver.chromium.org/downloads' same as your chrome browser version
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

input('Enter Any Key To Continue >>> ')

option=Options()
option.add_argument('user-data-dir=selenium')

# Open Chrome Browser with help of ChromeDriver and Selenium
driver = webdriver.Chrome('Enter your chrome browser path here' , options=option)
time.sleep(3)

def signup(email,fullName,userName,password):
    driver.get('https://www.instagram.com/accounts/emailsignup/?hl=en')
    time.sleep(4)

    #enter Xpath of email Field
    enter_email = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
    enter_email.clear()
    enter_email.send_keys(email)
    time.sleep(4)

    #enter Xpath of Name Field
    enter_fullName = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input')
    enter_fullName.clear()
    enter_fullName.send_keys(fullName)
    time.sleep(4)

    #enter Xpath of userName Field
    enter_userName = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input')
    enter_userName.clear()
    enter_userName.send_keys(userName)
    time.sleep(4)

    #enter Xpath of password Field
    enter_password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input')
    enter_password.clear()
    enter_password.send_keys(password)
    time.sleep(4)

    signUp = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button')
    time.sleep(4)
    signUp.click()

signup('email','fullName','username','password')    