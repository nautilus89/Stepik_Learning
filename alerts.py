from selenium import webdriver
import time
import math


def calc(x):
    return math.log(abs(12*math.sin(x)))


def alert_1():
    link = "http://suninjuly.github.io/alert_accept.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        confirm = browser.switch_to.alert
        confirm.accept()
        # time.sleep(1)
        value = calc(int(browser.find_element_by_id("input_value").text))
        browser.find_element_by_id("answer").send_keys(str(value))
        browser.find_element_by_css_selector("button.btn").click()
    finally:
        time.sleep(5)
        browser.quit()