import pytest
from lib.pages.HomePage import HomePage

class TestHomePage:
    @pytest.fixture(autouse=True)
    def setup_pageobjects(self, create_homepageobj):
        self.home_page = create_homepageobj

    def test_navigation_links_visible(self):
        assert self.home_page.verify_navigation_links_visible()

    def test_homepage_content_titles(self):
        titles = self.home_page.get_content_titles()

        assert titles[0] == 'COLLECT THE PLAYOFFS ON NBA TOP SHOT'
        assert titles[1] == 'NEVER MISS A MOMENT'
        assert titles[2] == 'START YOUR COLLECTION'

    def test_homepage_content_buttons(self):
        buttons = self.home_page.get_content_buttons()

        assert buttons[0] == 'SHOP PLAYOFFS MOMENTS'
        assert buttons[1] == 'SHOP PLAYOFFS MOMENTS'
        assert buttons[4] == 'BUY A PACK'

    def test_navigating_to_marketplace(self):
        self.home_page.goto_page('Marketplace')

        assert self.home_page.get_current_url() == 'https://nbatopshot.com/marketplace'



