import time

import config
import unittest
import logging
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка логирования
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class TestChangePassword(unittest.TestCase):
    def setUp(self):
        # Инициализация веб-драйвера (например, Firefox)
        self.driver = webdriver.Chrome()
        self.driver.get(config.MAIN_URL)
        logging.info(f"Открыт сайт: {config.MAIN_URL}")

    def generate_random_password(self, length=12):
        """Генерация случайного пароля."""
        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choice(characters) for i in range(length))

    def test_change_password(self):
        driver = self.driver

        # Переход к авторизации
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

        # Ожидание перехода на главную страницу
        logging.info("Ожидание появления аватара пользователя на главной странице.")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img.avatar"))
        )

        # Переход в личный кабинет
        logging.info("Переход в личный кабинет.")
        login_link = driver.find_element(By.CSS_SELECTOR, "img.avatar")
        login_link.click()

        try:
            # Переход в настройки профиля
            logging.info("Переход в настройки безопасности.")
            driver.find_element(By.LINK_TEXT, "Безопасность").click()

            # Ожидание кнопки для смены пароля
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.link"))
            )
            logging.info("Клик по кнопке изменения пароля.")
            driver.find_element(By.CSS_SELECTOR, "button.link").click()

            # Заполнение полей для смены пароля
            logging.info(f"Текущий пароль: {config.AUTH_PASSWORD_CORRECT}")
            old_password_input = driver.find_element(By.ID, "updatepasswordform-password")
            old_password_input.send_keys(config.AUTH_PASSWORD_CORRECT)

            # Генерация и установка нового пароля
            config.AUTH_PASSWORD_OLD = config.AUTH_PASSWORD_CORRECT
            config.AUTH_PASSWORD_CORRECT = self.generate_random_password()
            logging.info(f"Сгенерированный новый пароль: {config.AUTH_PASSWORD_CORRECT}")
            config.update_config(config.AUTH_PASSWORD_OLD, config.AUTH_PASSWORD_CORRECT)

            new_password_input = driver.find_element(By.ID, "updatepasswordform-new_password")
            new_password_input.send_keys(config.AUTH_PASSWORD_CORRECT)

            new_password_input_repeat = driver.find_element(By.ID, "updatepasswordform-new_password_repeat")
            new_password_input_repeat.send_keys(config.AUTH_PASSWORD_CORRECT)

            # Сохранение нового пароля
            save_button = driver.find_element(By.ID, "save-btn")
            save_button.click()
            logging.info("Новый пароль сохранен.")

            # Проверка успешного изменения пароля
            logging.info("Ожидание сообщения об успешном изменении пароля.")
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".alert--success"))
            )

            self.assertEqual("Да! Ваш пароль обновлен.", success_message.text)
            logging.info("Смена пароля прошла успешно.")

        except Exception as e:
            logging.error(f"Произошла ошибка при смене пароля: {e}")
            raise

    def test_change_password_wrong_repeat(self):
        driver = self.driver

        # Переход к авторизации
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

        # Ожидание перехода на главную страницу
        logging.info("Ожидание появления аватара пользователя на главной странице.")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img.avatar"))
        )

        # Переход в личный кабинет
        logging.info("Переход в личный кабинет.")
        login_link = driver.find_element(By.CSS_SELECTOR, "img.avatar")
        login_link.click()

        try:
            # Переход в настройки профиля
            logging.info("Переход в настройки безопасности.")
            driver.find_element(By.LINK_TEXT, "Безопасность").click()

            # Ожидание кнопки для смены пароля
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.link"))
            )
            logging.info("Клик по кнопке изменения пароля.")
            driver.find_element(By.CSS_SELECTOR, "button.link").click()

            # Заполнение полей для смены пароля
            logging.info(f"Текущий пароль: {config.AUTH_PASSWORD_CORRECT}")
            old_password_input = driver.find_element(By.ID, "updatepasswordform-password")
            old_password_input.send_keys(config.AUTH_PASSWORD_CORRECT)


            new_password_generated = self.generate_random_password()
            logging.info(f"Сгенерированный новый пароль: {new_password_generated}")


            new_password_input = driver.find_element(By.ID, "updatepasswordform-new_password")
            new_password_input.send_keys(new_password_generated)
            new_password_input_repeat = driver.find_element(By.ID, "updatepasswordform-new_password_repeat")
            new_password_input_repeat.send_keys(new_password_generated + "1")

            # Сохранение нового пароля
            save_button = driver.find_element(By.ID, "save-btn")
            save_button.click()
            logging.info("Введён неверный пароль.")

            # Проверка успешного изменения пароля
            logging.info("Ожидание сообщения об неудачном изменении пароля.")
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".has-error"))
            )

            self.assertTrue(error_message.is_displayed())
            logging.info("Смена пароля прошла не успешно.")

        except Exception as e:
            logging.error(f"Произошла ошибка при смене пароля: {e}")
            raise



    def tearDown(self):
        # Закрытие браузера
        logging.info("Закрытие браузера.")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
