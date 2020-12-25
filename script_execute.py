from selenium import webdriver
import time
import math


def script_1():
    try:
        browser = webdriver.Chrome()
        browser.execute_script("document.title='Script executing';alert('Robots at work');")
    finally:
        time.sleep(3)
        browser.quit()


def script_2():
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(3)
    # Эта команда проскроллит страницу на 100 пикселей вниз:
    # browser.execute_script("window.scrollBy(0, 100);")


def script_3():
    link = "http://suninjuly.github.io/execute_script.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        x = int(browser.find_element_by_id("input_value").text)
        answer = math.log((abs(12*math.sin(x))))
        answer_edit = browser.find_element_by_id("answer")
        answer_edit.send_keys(str(answer))
        checkbox = browser.find_element_by_id("robotCheckbox")
        browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
        checkbox.click()
        radio = browser.find_element_by_id("robotsRule")
        radio.click()
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    finally:
        time.sleep(5)
        browser.quit()