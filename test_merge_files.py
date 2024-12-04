import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import config


class TestMergePDF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Инициализация веб-драйвера (используем ChromeDriver)
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_merge_pdf_files(self):
        driver = self.driver

        # Шаг 1: Перейти на страницу "Объединить PDF"
        driver.get(config.MERGE_URL)

        # Шаг 2: Нажать на "Выбрать PDF файлы"
        upload_button = driver.find_element(By.ID, "pickfiles")
        upload_button.click()


        time.sleep(10)
        # Шаг 4: Нажать "Объединить PDF"
        merge_button = driver.find_element(By.ID, "processTask")
        merge_button.click()
        time.sleep(4)  # Ожидание завершения процесса

        # Шаг 5: Проверить наличие кнопки для скачивания
        download_button = driver.find_element(By.CSS_SELECTOR, "a.downloader__btn")
        self.assertTrue(download_button.is_displayed(), "Кнопка скачивания не отображается")

        download_button.click()
        time.sleep(5)  # Ожидание завершения скачивания

    def test_delete_merged_pdf_files(self):
        driver = self.driver
        driver.get("https://www.ilovepdf.com/ru/merge_pdf")
        self.assertIn("Объединить PDF файлы", driver.title, "Заголовок страницы не соответствует")

        # Шаг 2: Нажать на "Выбрать PDF файлы"
        upload_button = driver.find_element(By.ID, "pickfiles")
        upload_button.click()

        time.sleep(10)
        # Шаг 4: Нажать "Объединить PDF"
        merge_button = driver.find_element(By.ID, "processTask")
        merge_button.click()
        time.sleep(4)  # Ожидание завершения процесса

        # Шаг 5: Проверить наличие кнопки для скачивания
        delete_button = driver.find_element(By.ID, "delete")
        self.assertTrue(delete_button.is_displayed(), "Кнопка удаления не отображается")

        delete_button.click()

    def test_wrong_format_to_merge(self):
        driver = self.driver
        driver.get("https://www.ilovepdf.com/ru/merge_pdf")
        self.assertIn("Объединить PDF файлы", driver.title, "Заголовок страницы не соответствует")

        # Шаг 2: Нажать на "Выбрать PDF файлы"
        upload_button = driver.find_element(By.ID, "pickfiles")
        upload_button.click()
        time.sleep(10)
        error_toast = driver.find_element(By.CSS_SELECTOR, ".toast-error")
        self.assertTrue(error_toast.is_displayed())



    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()



if __name__ == "__main__":
    unittest.main()
