from selenium import webdriver

def browser_factory(browser_name):
    if browser_name.lower() == "chrome":
        # Launch Chrome browser
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name.lower() == "edge":
        # Launch Microsoft Edge browser
        edge_options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=edge_options)
    elif browser_name.lower() == "firefox":
        # Launch Firefox browser
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError("Invalid browser name. Supported browsers are: Chrome, Edge, Firefox")
    return driver