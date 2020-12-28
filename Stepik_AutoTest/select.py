from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time


def summ(x, y):
    return x + y


def select_1():
    link = "http://suninjuly.github.io/selects1.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        num_1 = int(browser.find_element_by_id("num1").text)
        num_2 = int(browser.find_element_by_id("num2").text)
        answer = summ(num_1, num_2)
        select = Select(browser.find_element_by_id("dropdown"))
        select.select_by_value(str(answer))
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    finally:
        time.sleep(5)
        browser.quit()
