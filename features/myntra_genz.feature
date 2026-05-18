Feature: Myntra GenZ Shopping Category Validations

  Scenario: Verify Women Western Wear Dresses End to End
    Given The automation browser is initialized and user navigates to home
    When The user searches for GenZ category item "Women Dresses"
    And Selects the first product item card from the search results grid
    And Selects an available apparel size configuration item option
    And Clicks on the add item to checkout bag submission option
    Then The application should update browser context routing direct to "checkout/cart"