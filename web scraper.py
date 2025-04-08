from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

driver = webdriver.Edge()
driver.get('https://neal.fun/sun-vs-moon')
driver.maximize_window() # Maximize Window

sleep(2.5) # Wait for page to load

cookies = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p') # Find cookies
cookies.click() # Click cookies

sleep(1)

moon = driver.find_element(By.ID, 'moon-btn') # Find moon button

while True:
    moon.click()
