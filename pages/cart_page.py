from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    actual = (By.CSS_SELECTOR, ".lfA-Dem")
    expected = 'Your cart is empty'

    def verify_cart_empty(self):
        self.verify_text(self.expected, *self.actual)

