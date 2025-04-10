import os
import time
import logging
from selenium import webdriver
from selenium.webdriver import (ChromeOptions,
                                FirefoxOptions,
                                EdgeOptions
                                )


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
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--enable-automation")
        options.add_argument("--window-size=1920,1080")
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
    elif browser == 'edge':
        options = EdgeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--enable-automation")
        options.add_argument("--window-size=1920,1080")
    else:
        raise ValueError("Invalid broswer type")
    
    driver = webdriver.Remote(
        command_executor=selenium_hub_url,
        options=options
    )
    
    print("Successfully connected to Selenium Grid")
    return driver
