import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Get Selenium Grid URL from environment variable
selenium_hub_url = os.environ.get('SELENIUM_HUB_URL', 'http://selenium-hub:4444/wd/hub')

def get_webdriver():
    """Create and return a new WebDriver instance connected to Selenium Grid."""
    try:
        logger.info(f"Attempting to connect to Selenium Grid at {selenium_hub_url}")
        
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # Using the updated approach for Selenium 4
        # Connect to the Selenium Grid hub
        driver = webdriver.Remote(
            command_executor=selenium_hub_url,
            options=options
        )
        
        logger.info("Successfully connected to Selenium Grid")
        return driver
    
    except Exception as e:
        logger.error(f"Failed to connect to Selenium Grid: {e}")
        # Sleep before retry
        time.sleep(5)
        return None

def run_simple_test(driver):
    """Run a simple test to verify the WebDriver is working."""
    try:
        # Navigate to a test page
        driver.get("https://www.example.com")
        logger.info(f"Page title: {driver.title}")
        
        # Find an element
        element = driver.find_element(By.TAG_NAME, "h1")
        logger.info(f"Found h1 element with text: {element.text}")
        
        return True
    except Exception as e:
        logger.error(f"Test execution failed: {e}")
        return False

def main():
    """Main function that runs in an infinite loop."""
    logger.info("Starting Selenium test container")
    
    iteration = 1
    
    while True:
        logger.info(f"Test iteration #{iteration}")
        
        # Get a new WebDriver instance
        driver = None
        retry_count = 0
        
        while not driver and retry_count < 5:
            driver = get_webdriver()
            if not driver:
                retry_count += 1
                logger.warning(f"Retrying connection ({retry_count}/5)...")
        
        if driver:
            try:
                # Run a simple test
                success = run_simple_test(driver)
                logger.info(f"Test {'passed' if success else 'failed'}")
                
                # Clean up
                driver.quit()
                logger.info("WebDriver closed")
                
            except Exception as e:
                logger.error(f"Error during test execution: {e}")
                # Attempt to clean up
                try:
                    driver.quit()
                except:
                    pass
        else:
            logger.error("Failed to connect to Selenium Grid after multiple attempts")
        
        # Wait before the next iteration
        wait_time = 10  # seconds
        logger.info(f"Waiting {wait_time} seconds before next iteration...")
        time.sleep(wait_time)
        
        iteration += 1

if __name__ == "__main__":
    # Add a small delay on startup to ensure the grid is ready
    time.sleep(5)
    main()