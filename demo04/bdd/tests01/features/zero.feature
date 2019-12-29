Feature: Compute factorial
  In order to play with Lettuce
  As beginners
  We'll implement factorial

  Scenario: Factorial of 0
    Given I have the numbern 0
    When I compute its factorial
    Then I see the number 1