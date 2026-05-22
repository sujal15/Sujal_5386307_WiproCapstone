Feature: Myntra GENZ Shopping Automation

Scenario: Women's Dresses E2E

Given user opens Myntra
When user hovers GENZ
And user clicks dresses
Then products should be visible
And user opens first product
And user selects size
And user adds to bag
And user opens bag
And user verifies item in bag
And user clicks place order

Scenario: Men's T-Shirts Positive
Given user opens Myntra
When user hovers GENZ
And user clicks mens tshirts
Then products should be visible

Scenario: Men's Kurtas Positive
Given user opens Myntra
When user hovers GENZ
And user clicks mens kurtas
Then products should be visible

Scenario: Men's Shoes Positive
Given user opens Myntra
When user hovers GENZ
And user clicks mens shoes
Then products should be visible

Scenario: Beauty Skincare Positive
    Given user opens Myntra
    When user hovers GENZ
    And user clicks skincare
    Then products should be visible




Scenario: Jewellery Negative
Given user opens Myntra
When user hovers GENZ
And user clicks jewellery
Then jewellery negative validation passes

Scenario: Heels Negative
    Given user opens Myntra
    When user hovers GENZ
    And user clicks heels
    Then heels negative validation passes