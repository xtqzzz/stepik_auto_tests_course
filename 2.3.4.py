from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text

    input = browser.find_element(By.XPATH, '//*[@class="form-control"]')
    input.send_keys(str(math.log(abs(12*math.sin(int(x))))))

    submit = browser.find_element(By.XPATH, '//*[@type="submit"]')
    submit.click()


finally:
    time.sleep(10)
    browser.quit()