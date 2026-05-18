# TC-07 | Negative | Women's Footwear -> Heels

Feature: Women's Footwear - Heels Negative Scenarios
  As a QA engineer
  I want to verify that unavailable sizes and invalid coupons are handled correctly
  So that users receive clear error feedback

  Background:
    Given I launch the Myntra website
    And I navigate to the GENZ section

  @negative @tc07 @womens-footwear
  Scenario: Unavailable shoe size is grayed out and Add to Bag is disabled
    When I click on "Women's Footwear" category
    And I select "Heels" sub-category
    Then the Heels listing page should load successfully

    When I click on the first available product
    And I select an unavailable size "UK 3"
    Then the size option should appear grayed out or marked unavailable
    And the "Add to Bag" button should be disabled

  @negative @tc07 @womens-footwear
  Scenario: Invalid coupon code shows error message at checkout
    When I click on "Women's Footwear" category
    And I select "Heels" sub-category
    And I click on the first available product
    And I select an available size on the product page
    And I click "Add to Bag"
    And I click on the bag and proceed to checkout
    When I enter an invalid coupon code "INVALIDXYZ999"
    And I apply the coupon
    Then an error message should be displayed for the invalid coupon
    And the total price should remain unchanged
