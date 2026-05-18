# TC-01 | E2E | Women's Western Wear -> Dresses
# Covers the full shopping journey from landing to checkout validation

Feature: E2E Shopping Flow - Women's Western Wear Dresses
  As a GenZ shopper on Myntra
  I want to browse and purchase Dresses from Women's Western Wear
  So that I can complete an end-to-end shopping experience

  Background:
    Given I launch the Myntra website
    And I navigate to the GENZ section

  @e2e @tc01 @smoke
  Scenario: Complete end-to-end purchase flow for Women's Western Wear - Dresses
    When I click on "Women's Western Wear" category
    And I select "Dresses" sub-category
    Then the Dresses listing page should load with products

    When I apply filter "Size" with value "M"
    And I apply filter "Price Range" with min "500" and max "3000"
    Then the product count should update after filtering

    When I click on the first available product
    Then the product detail page should display name, price and images

    When I select size "M" on the product page
    And I click "Add to Bag"
    Then the bag icon count should increase by 1

    When I click on the bag and proceed to checkout
    Then the checkout page should display the selected product details
    And the total amount should match the product price
