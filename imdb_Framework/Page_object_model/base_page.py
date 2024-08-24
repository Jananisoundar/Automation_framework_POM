from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        # Initialize with WebDriver instance
        self.driver = driver

    def scroll_to_element(self, locator, timeout=30):
        # Scroll to the element specified by the locator
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_element(self, locator, timeout=20):
        # Click the element specified by the locator
        element = self.find_element(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=20):
        # Enter text into the input field specified by the locator
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def find_element(self, locator, timeout=20):
        # Find an element specified by the locator
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_clickable(self, locator, timeout=20):
        # Wait until the element specified by the locator is clickable
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def get_current_url(self):
        # Get the current URL of the page
        return self.driver.current_url
