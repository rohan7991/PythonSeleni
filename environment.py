import os
import time
import allure
from allure_behave.hooks import allure_report
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from allure_commons._allure import attach
from configs.properties import Properties
from steps.before_signIn_step import driver_variables, login_obj
from browserselection import browsersetup
from allure_behave.hooks import allure_report
from allure_commons.types import AttachmentType
browser_obj = browsersetup
from allure import step
import allure

def before_all(context):
    print("Performing initial set up, invoking browser")
    driver_variables.append(browser_obj.browser_factory(Properties.browser_type))
    driver_variables[0].maximize_window()
    driver_variables[0].delete_all_cookies()
def before_feature(context, feature):
    if "Auto_user1" in feature.tags:
        driver_variables[0].refresh()
        time.sleep(5)
        login_obj.launchURL(driver_variables[0])
    #     login_obj.login_check(driver_variables[0])
    else:
        print("Tag Id which you entered is not in the list")
# def after_feature(context, feature):
#     login_obj.logout(driver_variables[0])
def save_screenshot(context, scenario):
    if scenario.status == 'passed':
        screenshot_name = "scenarioPassed" + scenario.name + ".png"
        screenshot_dir = "screenshots/passed_screenshots"
    else:
        screenshot_name = "scenarioFailed" + scenario.name + ".png"
        screenshot_dir = "screenshots/failed_screenshots"
    # Create the directory if it doesn't exist
    os.makedirs(screenshot_dir, exist_ok=True)
    # Specify the full path for the screenshot
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)
    # Save the screenshot
    driver_variables[0].save_screenshot(screenshot_path)
    return screenshot_path
def after_scenario(context, scenario):
    screenshot_path = save_screenshot(context, scenario)
    with step("Attach Screenshot"):
        attach.file(screenshot_path, name="Screenshot_2", attachment_type=AttachmentType.PNG)
def after_all(context):
    driver_variables[0].quit()