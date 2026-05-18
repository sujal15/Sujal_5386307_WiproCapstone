# TC-04 | Positive | Men's Footwear -> Casual Shoes

Feature: Men's Footwear - Casual Shoes Filter Validation
  As a GenZ shopper
  I want to filter Casual Shoes by brand and price
  So that I find shoes within my preference and budget

  Background:
    Given I launch the Myntra website
    And I navigate to the GENZ section

  @positive @tc04 @mens-footwear
  Scenario: Filter casual shoes by brand and price range
    When I click on "Men's Footwear" category
    And I select "Casual Shoes" sub-category
    Then the Casual Shoes listing page should load successfully

    When I apply filter "Brand" with value "Nike"
    And I apply filter "Price Range" with min "1000" and max "5000"
    Then the displayed products should match the brand filter
    And all displayed prices should be within the selected range

  @positive @tc04 @mens-footwear
  Scenario: Verify size chart opens on product detail page
    When I click on "Men's Footwear" category
    And I select "Casual Shoes" sub-category
    And I click on the first available product
    Then the product detail page should display name, price and images
    When I click on "Size Chart"
    Then the size chart popup should open
    And the size chart should display at least one size option
