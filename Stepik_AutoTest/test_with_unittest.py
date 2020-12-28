import unittest
from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestFormRegistration(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(fill_form_registration(link1), "Congratulations! You have successfully registered!",
                         "Should be absolute value of a number")

    def test_reg2(self):
        self.assertEqual(fill_form_registration(link2), "Congratulations! You have successfully registered!",
                         "Should be absolute value of a number")


# заполнение формы регистрации
def fill_form_registration(link):

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
        return welcome_text_elt.text

    finally:
        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
