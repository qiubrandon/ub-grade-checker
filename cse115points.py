from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import * 

root = Tk()
root.geometry('800x600')
root.title("Current Points in CSE 115")
Label(root, text = "Points: ",font = ("Helvetica", 50)).grid(row = 0, column = 0)





browser = webdriver.Chrome('C:/Users/brandon pc/Downloads/chromedriver')
browser.get('https://ublearns.buffalo.edu/')
bigLogin = browser.find_element(By.CLASS_NAME, 'login').click()
username = browser.find_element(By.XPATH, '//input[@id="login"]')
time.sleep(.25)
username.send_keys('')
time.sleep(.25)
password = browser.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys('')
browser.find_element(By.XPATH, '//input[@id="login-button"]').click()
time.sleep(2.5)
browser.switch_to.frame(browser.find_element(By.ID,'duo_iframe'))
# duo mobile section
# try:
#     browser.find_element(By.XPATH, '//button[@class="auth-button positive"]').click()
# except:
#     browser.find_element(By.XPATH, '//button[@class="positive auth-button"]').click()
passcode = browser.find_element(By.XPATH, '/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[2]/button')
passcode.click()
textbox = browser.find_element(By.CLASS_NAME, 'passcode-input')
time.sleep(.1)
textbox.send_keys("")
time.sleep(.1)
passcode.click()
# clicks on grades
try:
    element_present = EC.presence_of_element_located((By.ID, '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[8]/div/li/a/ng-switch/div/span'))
    WebDriverWait(browser, 3).until(element_present)
except TimeoutException:
    print("timed out! :(")
browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/bb-base-layout/div/aside/div[1]/nav/ul/bb-base-navigation-button[8]/div/li/a/ng-switch/div/span').click()
time.sleep(3)
# finds the grade for cse115
points = browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/div[1]/div/div[3]/div/div/div[3]/div/div/div[2]/div/bb-base-grades-student/div/div/div[2]/div[1]/bb-student-column[1]/div/div[2]/span/bb-display-grade-pill/div/div/div/span/bdi')
csepoints = points.get_attribute('innerHTML')

Label(root, text = csepoints, font = ("Helvetica", 50)).grid(row = 1, column = 0)
root.mainloop()