import pytest
from Page_object_model.search_page import SearchPage


@pytest.mark.usefixtures("setup")
class TestSearchResults:
    # Test class for verifying search results on the IMDb Search page

    def test_search_results(self):
        # Initialize the SearchPage with the WebDriver instance
        search_page = SearchPage(self.driver)

        # Scroll to the 'Name' element on the page
        search_page.scroll_to_name()

        # Click on the 'Name' element
        search_page.click_on_name()

        # Enter 'Ani' into the Name textbox
        search_page.enter_name_in_textbox("Ani")

        # Click the 'See results' button
        search_page.click_see_results()
