from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(6)


@when('Click on Cart Icon')
def click_on_cart(context):
    context.app.main_page.click_cart_icon()
    sleep(6)


@then('Verify "Your cart is empty"')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()
    context.driver.quit()
