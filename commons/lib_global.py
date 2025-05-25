from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def click_element(context, locator_type, locator_value):
    if locator_type == "xpath":
        context.find_element(By.XPATH, locator_value).click()
    elif locator_type == "class":
        context.find_element(By.CLASS_NAME, locator_value).click()
    elif locator_type == "id":
        context.find_element(By.ID, locator_value).click()
    else:
        raise ValueError("Unsupported locator type: " + locator_type)

def send_keys(context, locator_type, locator_value, send_keys_value):
    if locator_type == "xpath":
        context.find_element(By.XPATH, locator_value).send_keys(send_keys_value)
    elif locator_type == "class":
        context.find_element(By.CLASS_NAME, locator_value).send_keys(send_keys_value)
    elif locator_type == "id":
        context.find_element(By.ID, locator_value).send_keys(send_keys_value)
    else:
        raise ValueError("Unsupported locator type: " + locator_type)

def clear(context, locator_type, locator_value):
    if locator_type == "xpath":
        context.find_element(By.XPATH, locator_value).clear()
    elif locator_type == "class":
        context.find_element(By.CLASS_NAME, locator_value).clear()
    elif locator_type == "id":
        context.find_element(By.ID, locator_value).clear()
    else:
        raise ValueError("Unsupported locator type: " + locator_type)

# GetText Element
def getText(context, locator_type, locator_value):
    if locator_type == "xpath":
        getTextValue = context.find_element(By.XPATH, locator_value).text
        return getTextValue
    elif locator_type == "class":
        getTextValue = context.find_element(By.XPATH, locator_value).text
        return getTextValue
    elif locator_type == "id":
        getTextValue = context.find_element(By.XPATH, locator_value).text
        return getTextValue
    else:
        raise ValueError("Unsupported locator type: " + locator_type)

# Verify the element is displayed or not
def is_displayed(context, locator_type, locator_value):
    if locator_type == "xpath":
        context.find_element(By.XPATH, locator_value).is_displayed()
    elif locator_type == "class":
        context.find_element(By.XPATH, locator_value).is_displayed()
    elif locator_type == "id":
        context.find_element(By.XPATH, locator_value).is_displayed()
    else:
        raise ValueError("Unsupported locator type: " + locator_type)

# Find element and store
def find_element_locator(context, locator_type, locator_value):
    if locator_type == "xpath":
        element = context.find_element(By.XPATH, locator_value)
    elif locator_type == "class":
        element = context.find_element(By.XPATH, locator_value)
    elif locator_type == "id":
        element = context.find_element(By.XPATH, locator_value)
    else:
        raise ValueError("Unsupported locator type: " + locator_type)
    return element

def find_elements_locator(context, locator_type, locator_value):
    if locator_type == "xpath":
        element = context.find_elements(By.XPATH, locator_value)
    elif locator_type == "class":
        element = context.find_elements(By.XPATH, locator_value)
    elif locator_type == "id":
        element = context.find_elements(By.XPATH, locator_value)
    else:
        raise ValueError("Unsupported locator type: " + locator_type)
    return element

def not_displayed(context, locator_type, locator_value):
    if locator_type == "xpath":
        try:
            # Find the element by its XPath (replace with the correct locator)
            CurrentAccountelement = context.find_element(By.XPATH, locator_value)
            # Check if the element is NOT displayed
            is_not_displayed = not CurrentAccountelement.is_displayed()
            if is_not_displayed:
                print("Element is not displayed.")
            else:
                print("Element is displayed.")
        except NoSuchElementException:
            print("Element not found or other exception occurred.")
    if locator_type == "class":
        try:
            # Find the element by its XPath (replace with the correct locator)
            CurrentAccountelement = context.find_element(By.CLASS_NAME, locator_value)
            # Check if the element is NOT displayed
            is_not_displayed = not CurrentAccountelement.is_displayed()
            if is_not_displayed:
                print("Element is not displayed.")
            else:
                print("Element is displayed.")
        except NoSuchElementException:
            print("Element not found or other exception occurred.")
    if locator_type == "id":
        try:
            # Find the element by its XPath (replace with the correct locator)
            CurrentAccountelement = context.find_element(By.ID, locator_value)
            # Check if the element is NOT displayed
            is_not_displayed = not CurrentAccountelement.is_displayed()
            if is_not_displayed:
                print("Element is not displayed.")
            else:
                print("Element is displayed.")
        except NoSuchElementException:
            print("Element not found or other exception occurred.")

def clear(context, locator_type, locator_value):
    if locator_type == "xpath":
        context.find_element(By.XPATH, locator_value).clear()
    elif locator_type == "class":
        context.find_element(By.CLASS_NAME, locator_value).clear()
    elif locator_type == "id":
        context.find_element(By.ID, locator_value).clear()
    else:
        raise ValueError("Unsupported locator type: " + locator_type)
    # select theaccount

# Verify the element is enabled or not
def is_enabled(context, locator_type, locator_value):
    if locator_type == "xpath":
        context.find_element(By.XPATH, locator_value).is_enabled()
    elif locator_type == "class":
        context.find_element(By.XPATH, locator_value).is_enabled()
    elif locator_type == "id":
        context.find_element(By.XPATH, locator_value).is_enabled()
    else:
        raise ValueError("Unsupported locator type: " + locator_type)

# Verify the element is selected or not
def is_selected(context, locator_type, locator_value):
    if locator_type == "xpath":
        context.find_element(By.XPATH, locator_value).is_selected()
    elif locator_type == "class":
        context.find_element(By.XPATH, locator_value).is_selected()
    elif locator_type == "id":
        context.find_element(By.XPATH, locator_value).is_selected()
    else:
        raise ValueError("Unsupported locator type: " + locator_type)