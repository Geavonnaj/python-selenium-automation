from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from behave import given, when, then


@given('Open target home page')
def open_target(context):
    context.app.main_page.open_main()


@when('Click sign in')
def click_signin(context):
    context.app.main_page.click_signin()


@when('Click sign in on Navigation Menu')
def click_signin_nav(context):
    context.app.signin_page.click_signin_nav()


@then('Verify sign in formed open')
def verify_form_open(context):
    context.app.signin_page.verify_form_open()
