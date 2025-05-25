@Auto_user1
Feature: LeetCode Automation
  Scenario Outline: User login with valid and invalid credentials

    Given the user click on SignIn button
    When the user enters "<username>" and "<password>"
    Then the user should be <expected_url>
    Examples:
      | username    | password    | expected_url |
      | user1  | pass1 | https://leetcode.com/accounts/login/ |