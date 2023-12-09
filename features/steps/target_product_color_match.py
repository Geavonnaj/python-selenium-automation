from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from behave import given, when, then
from time import sleep

SWATCH_COLOR_locator = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
TEXT_COLOR_locator = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given('Open target product 88345426 page')
def open_product_page(context):
    context.driver.get('https://www.target.com/p/A-88345426')
    sleep(6)


@then('Click through product color swatches')
def verify_color_match(context):
    expected_color_match = ['Brown', 'Oatmeal', 'Gray', 'Black']
    actual_color = []

    fetch_color_swatch = context.driver.find_elements(*SWATCH_COLOR_locator)
    for swatches in fetch_color_swatch:
        swatches.click()
        selected_text_color = context.driver.find_element(*TEXT_COLOR_locator).text.split('\n')[1]
        actual_color.append(selected_text_color)
    assert expected_color_match == actual_color, f'Expected {expected_color_match} did not match actual {actual_color}'
