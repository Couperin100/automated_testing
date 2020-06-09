Feature: Testing interactions when submitting a form.
  As a Automated Selenium tester.
  I want to use the Selenium test page.
  So that I can test that the page interactions work as expected.

  Background:
    Given I am on the Selenium Test Page

  Scenario Outline: I submit the form in its default state
    When I click on the submit button
    Then I should see the title 'Submitted Values'
    And I should not see a value for the username
    And I should not see a value for the password
    And I should see <value> on the results page
    Examples:
    | value                 |
    | Comments...           |
    | No Value for filename |
    | Hidden Field Value    |
    | cb3                   |
    | rd2                   |
    | ms4                   |
    | dd3                   |
    | submit                |


  Scenario: I submit the form with a username and password
    When I enter the username 'test_username' into the form
    And I enter the password 'test_password' into the form
    And I click on the submit button
    Then I should see the correct value for the username
    And I should see the correct value for the password

