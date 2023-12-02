from selenium.webdriver.common.by import By

from pages.base_page import Page

from time import sleep


class CartPage(Page):
    actual = (By.CSS_SELECTOR, ".lfA-Dem")
    expected = 'Your cart is empty'

    def verify_cart_empty(self):
        assert self.expected == self.find_element(*self.actual).text
        self.driver.quit()
