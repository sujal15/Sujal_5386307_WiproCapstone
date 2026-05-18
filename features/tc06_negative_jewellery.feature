# TC-06 | Negative | Accessories -> Jewellery

Feature: Accessories - Jewellery Negative Scenarios
  As a QA engineer
  I want to verify error handling in Jewellery section
  So that users see correct feedback for invalid actions

  Background:
    Given I launch the Myntra website
    And I navigate to the GENZ section

  @negative @tc06 @accessories
  Scenario: No results shown when conflicting filters applied
    When I click on "Accessories" category
    And I select "Jewellery" sub-category
    Then the Jewellery listing page should load successfully

    When I apply filter "Price Range" with min "0" and max "10"
    Then the page should display a "no products found" message
    Or the product count should be zero

  @negative @tc06 @accessories
  Scenario: Wishlist without login redirects to login page
    When I click on "Accessories" category
    And I select "Jewellery" sub-category
    And I click on the first available product
    When I click the wishlist heart icon on the product page without being logged in
    Then the user should be redirected to the login page
    Or a login prompt should be displayed

  @negative @tc06 @accessories
  Scenario: Out-of-stock product shows Notify Me option
    When I click on "Accessories" category
    And I select "Jewellery" sub-category
    And I open a product that is out of stock
    Then the "Add to Bag" button should not be enabled
    And a "Notify Me" or "Out of Stock" indicator should be visible
