from selenium import webdriver
import time
import os


def file_upload_1():
    link = "http://suninjuly.github.io/file_input.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element_by_css_selector("input[name='firstname']").send_keys("Alexander")
        browser.find_element_by_css_selector("input[name='lastname']").send_keys("Antonov")
        browser.find_element_by_css_selector("input[name='email']").send_keys("quark89@mail.ru")

        # абсолютные путь до каталога с файлом
        # print(os.path.abspath(os.path.dirname(__file__)))
        directory = os.path.abspath(os.path.dirname(__file__))
        # абсолютный путь до файла
        # print(os.path.abspath(__file__))
        file_name = "test_file.txt"
        file_path = os.path.join(directory, file_name)
        browser.find_element_by_css_selector("input[name='file']").send_keys(file_path)
        browser.find_element_by_css_selector("button.btn").click()
    finally:
        time.sleep(5)
        browser.quit()