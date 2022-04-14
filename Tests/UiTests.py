import logging
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebDriverSetup import WebDriverSetup
from selenium.common.exceptions import TimeoutException


class AltexTests(WebDriverSetup):
    # XPATH LOCATORS
    games_link = "https://altex.ro/jocuri-pc/cpl/"
    accept_cookies = "/html/body/div/div[3]/div/div/button/span/span"
    green_popup = "/html/body/div[2]/div[1]/div/div/div[2]/button"
    product_one = "/html/body/div/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li[1]/a/div[6]/button/span/span"
    product_two = "/html/body/div/div[2]/div[1]/main/div[2]/div/div[2]/div/ul[2]/li[2]/a/div[6]/button/span/span"
    cart_button = "/html/body/div[2]/div[2]/div[1]/main/ul/li/div[1]/div/div[2]/div[3]/a"
    cart_count = "/html/body/div/div[1]/div/div/div/div[2]/div/a/span[3]"
    remove_button_one = "/html/body/div/div[2]/div[1]/main/div[1]/section/div[1]/ul/li[1]/div/div/div[1]/ul/li/div/" + \
                        "div[2]/div/button[2]"
    remove_button_two = "/html/body/div[2]/div[2]/div[1]/main/div[1]/section/div[1]/ul/li/div/div/div[1]/ul/li/div/" + \
                        "div[2]/div/button[2]"

    def click(self, locator):
        driver = self.driver
        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locator))).click()
        except TimeoutException:
            logging.warning(f"Clickable element: {locator} timeout, closing test")
            driver.close()

    def test_add_and_remove(self):
        driver = self.driver
        driver.get(self.games_link)
        self.click(self.accept_cookies)
        self.click(self.product_one)
        self.click(self.green_popup)
        WebDriverWait(driver, 10).until(EC.url_contains("produs-adaugat-in-cos"))
        driver.execute_script("window.history.go(-1)")
        self.click(self.product_two)
        self.click(self.green_popup)
        self.click(self.cart_button)
        cart_count = driver.find_element(By.XPATH, self.cart_count).text
        self.assertEqual(cart_count, '2')
        self.click(self.remove_button_one)
        self.click(self.green_popup)
        cart_count = driver.find_element(By.XPATH, self.cart_count).text
        self.assertEqual(cart_count, '1')
        self.click(self.remove_button_two)
        self.click(self.green_popup)
        cart_count = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div/div[2]/div/a/span[3]").text
        self.assertEqual(cart_count, "")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
