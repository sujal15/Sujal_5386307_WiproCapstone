# TC-02 | Positive | Men's Casual Wear -> T-Shirts

Feature: Men's Casual Wear - T-Shirts Filter and Product Selection
  As a GenZ shopper
  I want to browse T-Shirts using filters
  So that I can find the right product

  Background:
    Given I launch the Myntra website
    And I navigate to the GENZ section

  @positive @tc02 @mens-casual
  Scenario: Browse and filter T-Shirts in Men's Casual Wear
    When I click on "Men's Casual Wear" category
    And I select "T-Shirts" sub-category
    Then the T-Shirts listing page should load successfully

    When I apply filter "Size" with value "L"
    Then the filtered results should display only matching products

    When I apply filter "Color" with value "Black"
    Then the product listing should update with the applied filters

    When I click on the first available product
    Then the product detail page should display name, price and images
    And the product page should show size options

  @positive @tc02 @mens-casual
  Scenario: Verify product count updates with filters in T-Shirts
    When I click on "Men's Casual Wear" category
    And I select "T-Shirts" sub-category
    And I note the initial product count
    When I apply filter "Brand" with value "HRX"
    Then the product count should be less than or equal to the initial count
    And at least one product should be displayed
