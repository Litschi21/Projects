import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time


def click():
    driver = webdriver.Edge()
    driver.get('https://hyperplexed.io/events/live-thumbnail')

    time.sleep(3)

    element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div/div[2]/div[2]/div/div/div/div[2]/button[5]/div[2]/i')
    while not keyboard.is_pressed('q'):
        element.click()


t1 = threading.Thread(target=click)
t2 = threading.Thread(target=click)

t1.start()
t2.start()

t1.join()
t2.join()
