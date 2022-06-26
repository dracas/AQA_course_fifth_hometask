Feature: practice form sub-tab

  Scenario: Click on Click Me button
    Given I'm on Forms page
    When I click on Practice Form sub-tub
    Then I see Student Registration Form
    And The form contains first name and last name fields
    And The form contains email field
    And The form contains gender field
    And The form contains mobile field
    And The form contains date of birth field
    And A format of date of birth field is dd mmm yyyy
    And The form contains hobby checkbox
    And The form contains button to upload pictures
    And The form contains current address field
    And The form contains state and city fields