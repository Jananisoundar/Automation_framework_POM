from selenium.webdriver.common.by import By
from Page_object_model.base_page import BasePage

class SearchPage(BasePage):

    # Locators for elements on the Search page
    NAME = (By.XPATH, "//div[contains(text(),'Name')]")
    NAME_TEXTBOX = (By.XPATH, "//input[@placeholder='e.g. Audrey Hepburn']")
    SEE_RESULTS = (By.XPATH, "//span[contains(text(), 'See results')]")

    def scroll_to_name(self):
        # Ensure the NAME element is present and then scroll to it
        self.find_element(self.NAME)
        self.scroll_to_element(self.NAME)
        print("Scrolled to NAME element")

    def click_on_name(self):
        # Click on the NAME element
        self.click_element(self.NAME)
        print("Clicked on NAME element")

    def enter_name_in_textbox(self, name):
        # Ensure the NAME_TEXTBOX element is present, scroll to it, and enter text
        self.find_element(self.NAME_TEXTBOX)
        self.scroll_to_element(self.NAME_TEXTBOX)
        print("Scrolled to NAME_TEXTBOX element")
        self.enter_text(self.NAME_TEXTBOX, name)
        print(f"Entered text '{name}' in NAME_TEXTBOX")

    def click_see_results(self):
        # Click on the SEE_RESULTS button
        self.click_element(self.SEE_RESULTS)
        print("Clicked on SEE_RESULTS button")
