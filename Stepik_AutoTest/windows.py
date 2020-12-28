from selenium import webdriver
import math
import time


def new_window():
    link = "http://suninjuly.github.io/redirect_accept.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        # handle текущего окна
        # first_window = browser.current_window_handle
        # или
        # first_window = browser.window_handles[0]
        browser.find_element_by_css_selector("button.trollface").click()
        browser.switch_to.window(browser.window_handles[1])
        value = int(browser.find_element_by_id("input_value").text)
        value = math.log(abs(12*math.sin(value)))
        browser.find_element_by_id("answer").send_keys(str(value))
        browser.find_element_by_css_selector("button.btn").click()
    finally:
        time.sleep(5)
        browser.quit()