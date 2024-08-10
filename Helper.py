from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def login_successfully(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    time.sleep(3)
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    time.sleep(3)
    context.driver.find_element(By.ID, 'login-button').click()
    time.sleep(3)