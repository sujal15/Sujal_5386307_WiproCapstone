from behave import given, when, then

from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


@given("user opens Myntra")
def step(context):

    context.home = HomePage(context.driver)
    context.category = CategoryPage(context.driver)
    context.product = ProductPage(context.driver)

    context.home.open_myntra()


@when("user hovers GENZ")
def step(context):

    context.home.hover_genz()


@when("user clicks dresses")
def step(context):

    context.home.click_women_dresses()
@then("user opens bag")
def step(context):

    context.product.open_bag()


@then("user verifies item in bag")
def step(context):

    context.product.verify_item_in_bag()


@then("user clicks place order")
def step(context):

    context.product.click_place_order()

@when("user clicks mens tshirts")
def step(context):

    context.home.click_mens_tshirts()


@when("user clicks mens kurtas")
def step(context):
    print("Executing Kurtas step")
    context.home.click_mens_kurtas()


@when("user clicks mens shoes")
def step(context):

    context.home.click_mens_shoes()

@when("user clicks skincare")
def step(context):

    context.home.click_skincare()

@when("user clicks jewellery")
def step(context):

    context.home.click_jewellery()


@then("products should be visible")
def step(context):

    context.category.verify_products_visible()


@then("user opens first product")
def step(context):

    context.category.open_first_product()
    context.product.switch_to_product_tab()


@then("user selects size")
def step(context):

    context.product.select_size()


@then("user adds to bag")
def step(context):

    context.product.add_to_bag()
    context.product.verify_add_to_bag()


@then("jewellery negative validation passes")
def step(context):

    wrong="Smartphones"

    assert wrong not in context.driver.title

    print("Negative test passed")


@when("user clicks heels")
def step(context):

    context.home.click_heels()


@then("heels negative validation passes")
def step(context):

    wrong = "Refrigerator"

    assert wrong not in context.driver.title

    print("Negative Test Passed")