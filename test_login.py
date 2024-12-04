import time

import config
import unittest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка логирования
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class TestLogin(unittest.TestCase):
    def setUp(self):
        # Инициализация веб-драйвера (например, Firefox)
        self.driver = webdriver.Firefox()
        self.driver.get(config.MAIN_URL)
        logging.info(f"Открыт сайт: {config.MAIN_URL}")


    def test_successful_login(self):
        driver = self.driver
        logging.info("Переход на страницу авторизации.")

        # Переход на страницу авторизации
        login_link = driver.find_element(By.CSS_SELECTOR, "a.link--secondary")
        login_link.click()


        logging.info("Клик по ссылке 'Войти'.")

        # Заполнение формы авторизации
        email_input = driver.find_element(By.ID, "loginEmail")
        password_input = driver.find_element(By.ID, "inputPasswordAuth")

        logging.info("Заполнение формы авторизации.")
        email_input.send_keys(config.AUTH_EMAIL_CORRECT)
        password_input.send_keys(config.AUTH_PASSWORD_CORRECT)

        # Отправка формы
        password_input.send_keys(Keys.RETURN)
        logging.info("Отправка формы авторизации.")
        time.sleep(2)
        self.assertTrue(
            driver.find_element(
                By.CSS_SELECTOR, "img.avatar"
            ).is_displayed(),
        )
        logging.info("Личный кабинет успешно отображается.")

    def test_unsuccessful_login(self):
        driver = self.driver
        logging.info("Переход на страницу авторизации.")

        # Переход на страницу авторизации
        login_link = driver.find_element(By.CSS_SELECTOR, "a.link--secondary")
        login_link.click()
        logging.info("Клик по ссылке 'Войти'.")


        # Заполнение формы авторизации с неправильными данными
        email_input = driver.find_element(By.ID, "loginEmail")
        password_input = driver.find_element(By.ID, "inputPasswordAuth")

        logging.info("Заполнение формы авторизации с неправильными данными.")
        email_input.send_keys(config.AUTH_EMAIL_CORRECT)
        password_input.send_keys(config.AUTH_PASSWORD_INVALID)

        # Отправка формы
        password_input.send_keys(Keys.RETURN)
        logging.info("Отправка формы авторизации с неправильными данными.")
        time.sleep(2)
        error_message = driver.find_element(By.CSS_SELECTOR, ".has-error")
        logging.info(error_message.text)
        logging.info(error_message.is_displayed())
        self.assertTrue(
            error_message.is_displayed(),
        )
        logging.info("Сообщение об ошибке успешно отображается.")

    def tearDown(self):
        # Закрытие браузера
        logging.info("Закрытие браузера.")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
