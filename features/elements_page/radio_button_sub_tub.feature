Feature: radio button sub-tub

  Scenario Outline: Verification of messages
    Given I'm on Elements page
    And I'm on Radio Button sub-tab
    When I select <button>
    Then I see message 'You have selected <button>'

    Examples:
    |button    |
    |Yes       |
    |Impressive|