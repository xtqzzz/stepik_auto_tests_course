from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    submit = browser.find_element(By.XPATH, "//button")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()