# TC-03 | Positive | Men's Occasion Wear -> Kurtas

Feature: Men's Occasion Wear - Kurtas Category Navigation
  As a GenZ shopper
  I want to browse Kurtas for occasions
  So that I can find occasion-appropriate clothing

  Background:
    Given I launch the Myntra website
    And I navigate to the GENZ section

  @positive @tc03 @mens-occasion
  Scenario: Navigate to Kurtas and verify category loads correctly
    When I click on "Men's Occasion Wear" category
    And I select "Kurtas" sub-category
    Then the Kurtas listing page should load successfully
    And product cards should display fabric and occasion tags

  @positive @tc03 @mens-occasion
  Scenario: Sort Kurtas by popularity and verify order
    When I click on "Men's Occasion Wear" category
    And I select "Kurtas" sub-category
    And I sort products by "Popularity"
    Then the product list should reorder without errors
    And at least one product should be displayed

  @positive @tc03 @mens-occasion
  Scenario: Apply occasion filter on Kurtas
    When I click on "Men's Occasion Wear" category
    And I select "Kurtas" sub-category
    And I apply filter "Occasion" with value "Festive"
    Then the filtered Kurtas should be displayed
    And the product attributes should be visible on each card
