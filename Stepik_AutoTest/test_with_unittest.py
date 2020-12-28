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
        browser.find_element_by_css_selector(".first_block .first").send_keys("Ivan")
        browser.find_element_by_css_selector(".first_block .second").send_keys("Petrov")
        browser.find_element_by_css_selector(".first_block .third").send_keys("ipetrov@test.ru")
        browser.find_element_by_css_selector("button.btn").click()

        time.sleep(2)

        # находим элемент, содержащий текст
        return browser.find_element_by_tag_name("h1").text
    finally:
        browser.quit()


if __name__ == "__main__":
    unittest.main()
