# conftest.py
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    """
    Fixture to set up and tear down the Selenium WebDriver instance for tests.

    :param request: Pytest request object to access the test class.
    """
    # Initialize the WebDriver instance (Chrome in this case)
    driver = webdriver.Chrome()  # You can replace with webdriver.Firefox(), etc.

    # Open the target URL
    driver.get("https://www.imdb.com/search/name/")

    # Maximize the browser window
    driver.maximize_window()

    # Attach the WebDriver instance to the test class
    request.cls.driver = driver

    # Yield control back to the test function
    yield

    # After test execution, quit the WebDriver instance
    driver.quit()
