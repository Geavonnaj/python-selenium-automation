from selenium.webdriver.common.by import By

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")

    def verify_search_result(self, product):
        self.verify_partial_text(product,*self.SEARCH_RESULT_TXT)

    def verify_search_url(self, expected_partial_url):
        assert expected_partial_url in self.driver.current_url, \
            f'Expected {expected_partial_url} not in {self.driver.current_url}'
