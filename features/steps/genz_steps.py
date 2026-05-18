from behave import given, when, then
from pages.home_page import HomePage
from pages.product_page import ProductPage

@given('The automation browser is initialized and user navigates to home')
def step_impl(context):
    context.driver.get("https://www.myntra.com")
    context.home_page = HomePage(context.driver)

@when('The user searches for GenZ category item "{item_name}"')
def step_impl(context, item_name):
    context.home_page.search_genz_category(item_name)
    context.product_page = ProductPage(context.driver)

@when('Selects the first product item card from the search results grid')
def step_impl(context):
    context.product_page.select_first_product()

@when('Selects an available apparel size configuration item option')
def step_impl(context):
    context.product_page.choose_available_size()

@when('Clicks on the add item to checkout bag submission option')
def step_impl(context):
    context.product_page.click_add_to_bag()
    context.product_page.go_to_checkout_bag()

@then('The application should update browser context routing direct to "{cart_url_path}"')
def step_impl(context, cart_url_path):
    assert cart_url_path in context.driver.current_url