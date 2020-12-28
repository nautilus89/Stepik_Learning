from selenium import webdriver
import time


# обычное заполнение формы
def fill_form():

    link = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id("country")
        input4.send_keys("Russia")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


# заполнение формы в цикле
def fill_form_in_circle():

    link = "http://suninjuly.github.io/huge_form.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fields = browser.find_elements_by_css_selector('*[type="text"]')
        for field in fields:
            field.send_keys("A")
        button = browser.find_element_by_class_name("btn")
        button.click()
    finally:
        time.sleep(10)
        browser.quit()


# заполнение формы с помощью xpath
def fill_form_xpath():

    link = "http://suninjuly.github.io/find_xpath_form"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id("country")
        input4.send_keys("Russia")

        button = browser.find_element_by_xpath('//button[text()="Submit"]')
        button.click()

    finally:
        time.sleep(5)
        browser.quit()


# заполнение формы регистрации 1
def fill_form_registration_1():

    link = "http://suninjuly.github.io/registration1.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("ipetrov@test.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(5)
        browser.quit()


# заполнение формы регистрации 2
def fill_form_registration_2():

    link = "http://suninjuly.github.io/registration2.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("ipetrov@test.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(5)
        browser.quit()