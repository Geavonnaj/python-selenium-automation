from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page

NAVBAR = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
SIGNIN_ICON = (By.CSS_SELECTOR, ".styles__LinkText-sc-1e1g60c-3")
FORM = (By.CSS_SELECTOR, "h1[class*='styles__StyledHeading']")


class Signin(Page):
    def click_signin_nav(self):
        self.find_element(*NAVBAR).click()

    def verify_form_open(self):
        expected = 'Sign into your Target account'
        actual = self.driver.find_element(*FORM).text
        assert expected == actual, f'Expected {expected} did not match {actual}'

