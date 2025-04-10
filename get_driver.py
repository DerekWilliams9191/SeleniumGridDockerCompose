import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Get Selenium Grid URL from environment variable
# Use 'http://selenium-hub:4444/wd/hub' as default value
selenium_hub_url = os.environ.get('SELENIUM_HUB_URL', 'http://selenium-hub:4444/wd/hub')

def get_webdriver(browser='chrome'):
    """Create and return a new WebDriver instance connected to Selenium Grid."""
    print(f"Attempting to connect to Selenium Grid at {selenium_hub_url}")

    broswer = browser.lower()
    if browser == 'chrome': 
        options = ChromeOptions()
        # If you add headless, you cannot see the browser in the VNC
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    elif browser == 'edge':
        options = EdgeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    else:
        raise ValueError("Invalid broswer type")
    
    driver = webdriver.Remote(
        command_executor=selenium_hub_url,
        options=options
    )
    
    print("Successfully connected to Selenium Grid")
    return driver
