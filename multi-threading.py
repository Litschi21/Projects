from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time

def click_moon(thread_num):
    print(f'Thread number {thread_num} is now running.')

    Options = webdriver.ChromeOptions()
    Options.add_argument('--headless=new')
    Options.add_argument('--window-size=1280, 700')

    driver = webdriver.Chrome()
    driver.get('https://neal.fun/sun-vs-moon')

    time.sleep(3)

    cookies = driver.find_element(By.CSS_SELECTOR, 'body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button')
    driver.execute_script("arguments[0].click();", cookies)

    time.sleep(0.5)

    moon = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]/div/button')
    for i in range(1000):
        driver.execute_script("arguments[0].click();", moon)


threads = []
max_threads = 2

for i in range(1, max_threads + 1):
    thread = threading.Thread(target=click_moon, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('Done!')
