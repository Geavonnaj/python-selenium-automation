from pages.base_page import Page
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import Signin


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.main_page = MainPage(driver)
        self.product_page = ProductPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.signin_page = Signin(driver)
