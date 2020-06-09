import pynput
import time
from pynput.mouse import Button, Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

mouse = Controller()

def sendmoney():
 username = input("What is your Paypal email?")
 username = username.replace(' ' , '')
 password = input("What is your Paypal account password")
 password = password.replace(' ', '')
 persontosend = input("Who are you going to send it to?")
 midamount = input("How much money would you like to send?")
 finalamount = midamount.replace('.' , '')
 PATH = "C:\Program Files (x86)\chromedriver.exe"
 driver = webdriver.Chrome(PATH)
 driver.get('https://www.paypal.com/signin?returnUri=https%3A%2F%2Fwww.paypal.com%2Fmyaccount%2Fsummary&state=')
 driver.find_element_by_name('login_email').send_keys(username)
 driver.find_element_by_name('btnNext').click()
 driver.implicitly_wait(3)
 driver.find_element_by_name('login_password').send_keys(password)
 driver.find_element_by_name('btnLogin').click()
 driver.implicitly_wait(3)
 driver.find_element_by_link_text("Send").click()
 driver.implicitly_wait(3)
 time.sleep(1)
 driver.find_element_by_name('autocomplete-input').send_keys(persontosend)
 driver.find_element_by_name('autocomplete-input').send_keys(Keys.ENTER)
 time.sleep(2)
 driver.implicitly_wait(3)
 mouse.position = (500, 575)
 time.sleep(2)
 mouse.click(Button.left, 2)
 driver.find_element_by_name('amount').send_keys(finalamount)
 driver.find_element_by_name('amount').send_keys(Keys.ENTER)
 driver.implicitly_wait(3)
 time.sleep(3)
 driver.find_element_by_xpath('//*[@id="react-transfer-container"]/div/div/div/button[1]').click()
 driver.implicitly_wait(3)
 driver.find_element_by_xpath('//*[@id="react-transfer-container"]/div/div/form/button[1]').click()
 time.sleep(60)


sendmoney()
