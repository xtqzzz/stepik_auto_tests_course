from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1')
    (t1) = num1.text
    num2 = browser.find_element(By.ID, 'num2')
    (t2) = num2.text
    print(int(t1) + int(t2))


    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(str(int(t1)+int(t2))))

    submit = browser.find_element(By.XPATH, '//*[@type="submit"]')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()