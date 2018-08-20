Feature: Plan a journey using the TFL website.
  As a user
  I want to use the journey planner.
  So that I can verify that I get the expected alerts

  Background:
    Given I am on the TFL website

  Scenario: I do not enter a station into the From field
    Given I leave the 'From' field empty
    When I click on the plan my journey button
    Then I should see the alert 'The From field is required'

  Scenario: I do not enter a station into the To field
    Given I leave the 'To' field empty
    When I click on the plan my journey button
    Then I should see the alert 'The To field is required'

  Scenario: I do not enter a station into the To or From field
    Given I leave the 'From' and 'To' field empty
    When I click on the plan my journey button
    Then I should see the alert 'The From field is required'
    And I should see the alert 'The To field is required'