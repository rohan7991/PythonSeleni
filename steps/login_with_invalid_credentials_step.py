from steps.before_signIn_step import driver_variables
# Import necessary modules
from behave import given, when, then
from pages.login_with_invalid_credentials_page import login_with_invalid_cred
login_obj = login_with_invalid_cred
# Step definitions
@given('the user click on SignIn button')
def step_display_login_page(context):
    login_obj.click_SignIn(driver_variables[0])
    # Your implementation to navigate to the login page
    pass
@when('the user enters "{username}" and "{password}"')
def step_enter_credentials(context, username, password):
    login_obj.send_username_and_password(driver_variables[0], username, password)
@then('the user should be {expected_url}')
def step_verify_login_result(context, expected_url):
    # Your implementation to verify login result
    result = driver_variables[0].current_url
    assert result == expected_url, f"Expected {expected_url}, but got {result}"