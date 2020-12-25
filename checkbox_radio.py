from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def checkbox_radio_1():
    link = "http://suninjuly.github.io/math.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x = browser.find_element_by_css_selector("#input_value")
        x = calc(int(x.text))
        answer = browser.find_element_by_css_selector("#answer")
        answer.send_keys(str(x))

        checkbox = browser.find_element_by_css_selector("#robotCheckbox")
        checkbox.click()

        radio = browser.find_element_by_css_selector("#robotsRule")
        radio.click()

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    finally:
        time.sleep(5)
        browser.quit()


def checkbox_radio_2():
    link = "http://suninjuly.github.io/get_attribute.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        treasure = browser.find_element_by_id("treasure")
        x = treasure.get_attribute("valuex")
        x = calc(x)
        answer = browser.find_element_by_id("answer")
        answer.send_keys(str(x))

        checkbox = browser.find_element_by_id("robotCheckbox")
        checkbox.click()

        radio = browser.find_element_by_id("robotsRule")
        radio.click()

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    finally:
        time.sleep(5)
        browser.quit()
