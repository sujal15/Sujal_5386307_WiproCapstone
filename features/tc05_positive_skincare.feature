# TC-05 | Positive | Beauty & Grooming -> Skincare

Feature: Beauty and Grooming - Skincare Product Validation
  As a GenZ shopper
  I want to browse and wishlist Skincare products
  So that I can save products for later purchase

  Background:
    Given I launch the Myntra website
    And I navigate to the GENZ section

  @positive @tc05 @beauty-grooming
  Scenario: Browse Skincare products with skin type filter
    When I click on "Beauty and Grooming" category
    And I select "Skincare" sub-category
    Then the Skincare listing page should load successfully

    When I apply filter "Skin Type" with value "Oily"
    Then the filtered skincare products should be displayed
    And at least one product should be displayed

  @positive @tc05 @beauty-grooming
  Scenario: View skincare product details and add to wishlist
    When I click on "Beauty and Grooming" category
    And I select "Skincare" sub-category
    And I click on the first available product
    Then the product detail page should display name, price and images

    When I click the wishlist heart icon on the product page
    Then a wishlist confirmation message should appear
    And the wishlist icon should be filled/active
