from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from behave import given, when, then
from time import sleep

INPUT_SEARCH = (By.CSS_SELECTOR, '#search')
SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test*='SearchButton']")
PRODUCT_TO_CART = (By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor15013944')
CART_ITEM = (By.CSS_SELECTOR, "h4[class='styles__StyledHeading-sc-1xmf98v-0 dQsNJZ']")


@given('Open targets home page')
def targets_url(context):
    context.app.main_page.open_main()


@when('Type {search_word} into search field')
def input_search(context, search_word):
    context.app.main_page.search()


@when('Add to cart')
def product_to_cart(context):
    context.app.product_page.add_product_to_cart()


@then('Verify {search_word} is added in cart')
def item_in_cart(context, search_word):
    context.app.product_page.verify_item_in_cart()
