from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductPage(Page):

    PRODUCT_TO_CART = (By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor15013944')
    CART_ITEM = (By.CSS_SELECTOR, "h4[class='styles__StyledHeading-sc-1xmf98v-0 dQsNJZ']")

    def add_product_to_cart(self):
        self.click(self, *self.PRODUCT_TO_CART)

    def verify_item_in_cart(self, search_word):
        self.verify_partial_text(self, search_word, *self.CART_ITEM)


