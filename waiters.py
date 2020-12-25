from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def wait_1():
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text


def wait_2():
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/cats.html")

    button = browser.find_element_by_id("button")
    button.click()


def wait_3():

    link = "http://suninjuly.github.io/explicit_wait2.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
        # assert price
        button = browser.find_element_by_id("book")
        button.click()
        x = browser.find_element_by_id("input_value").get_attribute()
        x = calc(int(x.text))
        answer = browser.find_element_by_id("answer")
        answer.send_keys(str(x))
        button2 = browser.find_element_by_id("solve")
        button2.click()
    finally:
        time.sleep(5)
        browser.quit()
