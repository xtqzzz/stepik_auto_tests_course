from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    input = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    browser.execute_script("window.scrollBy(0, 150);")

    checkbox = browser.find_element(By.XPATH, "//*[@type='checkbox']")
    checkbox.click()

    radio = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    radio.click()

    submit = browser.find_element(By.XPATH, "//*[@type='submit']")
    submit.click()


finally:
    time.sleep(5)
    browser.quit