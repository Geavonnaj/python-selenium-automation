from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "image[href='https://assets.targetimg1.com/icons/assets/glyph/Cart.svg#Cart']")
    SIGNIN_ICON = (By.CSS_SELECTOR, ".styles__LinkText-sc-1e1g60c-3")
    INPUT_SEARCH = (By.CSS_SELECTOR, '#search')
    PRODUCT_TO_CART = (By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor15013944')
    CART_ITEM = (By.CSS_SELECTOR, "h4[class='styles__StyledHeading-sc-1xmf98v-0 dQsNJZ']")

    def open_main(self):
        self.open_url('https://www.target.com/')

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)  # wait for ads to disappear

    def click_cart_icon(self):
        self.wait_for_element_click(*self.CART_ICON)
        element = self.wait_for_element_appear()
        element.send_keys

    def click_signin(self):
        self.driver.find_element(*self.SIGNIN_ICON).click()
