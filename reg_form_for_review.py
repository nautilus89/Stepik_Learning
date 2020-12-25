from selenium import webdriver
import time


# заполнение формы регистрации
def fill_form_registration():

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


# заполнение формы регистрации - чужие рецензии
def fill_form_registration_2():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input2 = browser.find_element_by_css_selector('[class="form-control first"][placeholder*="name"]')
        input2.send_keys("Sad")
        input4 = browser.find_element_by_css_selector('[class="form-control second"][placeholder*="name"]')
        input4.send_keys("check")
        input1 = browser.find_element_by_tag_name('[class="form-control third"][placeholder*="email"]')
        input1.send_keys("lol")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()