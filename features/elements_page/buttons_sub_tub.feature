Feature: buttons sub-tab

  Scenario: Click on Click Me button
    Given I'm on Elements page
    And I'm on Buttons sub-tab
    When I click on Click Me button
    Then I see 'You have done a dynamic click' message

  Scenario: Click on Double Click Me button
    Given I'm on Elements page
    And I'm on Buttons sub-tab
    When I do double-click on Double Click Me button
    Then I see 'You have done a double click' message