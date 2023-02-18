import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

book = browser.find_element(By.XPATH, "//button[@id='book']")
book.click()

x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(
    str(log(abs(12*sin(int(x)))))
)
browser.find_element(By.XPATH, '//button[@id="solve"]').click()
time.sleep(5)