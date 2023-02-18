from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sunduk = browser.find_element(By.ID, "treasure")
    x = sunduk.get_attribute("valuex")

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